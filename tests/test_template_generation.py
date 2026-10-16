import shutil
import subprocess
from pathlib import Path

import copier


def has_pnpm_in_path() -> bool:
    return shutil.which("pnpm") is not None


def run_node_command_in_docker(cwd: Path, cmd: str) -> None:
    """Fallback runner executing Node/pnpm inside container if local pnpm is absent."""
    docker_cmd = [
        "docker",
        "run",
        "--rm",
        "-v",
        f"{cwd}:/app",
        "-w",
        "/app",
        "node:20-alpine",
        "sh",
        "-c",
        f"corepack enable && corepack prepare pnpm@9 --activate && {cmd}",
    ]
    subprocess.run(docker_cmd, check=True)


def test_generate_standard_vue_spa(tmp_path: Path):
    target = tmp_path / "standard-vue-spa"
    template_root = Path(__file__).parent.parent

    copier.run_copy(
        src_path=str(template_root),
        dst_path=str(target),
        data={
            "app_name": "test-app-portal",
            "app_description": "Standard Test Frontend",
            "default_dev_port": 5173,
            "api_base_url_default": "/api",
            "include_pinia_store": True,
            "include_architecture_scaffold": True,
            "include_diataxis_docs": True,
        },
        defaults=True,
        unsafe=True,
    )

    # Core configuration files
    assert (target / "package.json").is_file()
    assert (target / "tsconfig.json").is_file()
    assert (target / "vite.config.ts").is_file()
    assert (target / "vitest.config.ts").is_file()
    assert (target / ".eslintrc.cjs").is_file()
    assert (target / "Dockerfile").is_file()
    assert (target / "nginx.conf").is_file()
    assert (target / ".env.example").is_file()

    # Feature-Sliced Design layout
    assert (target / "src" / "main.ts").is_file()
    assert (target / "src" / "App.vue").is_file()
    assert (target / "src" / "app" / "router" / "index.ts").is_file()
    assert (target / "src" / "pages" / "HomeView.vue").is_file()
    assert (target / "src" / "features" / "auth" / "AuthForm.vue").is_file()
    assert (target / "src" / "entities" / "user" / "model.ts").is_file()
    assert (target / "src" / "entities" / "user" / "store.ts").is_file()
    assert (target / "src" / "shared" / "ui" / "BaseButton.vue").is_file()
    assert (target / "src" / "shared" / "api" / "client.ts").is_file()

    # Boundary test & rulesets
    assert (target / "tests" / "architecture" / "test_boundaries.spec.ts").is_file()
    assert (target / "tests" / "unit" / "BaseButton.spec.ts").is_file()
    assert (target / "tests" / "unit" / "UserSchema.spec.ts").is_file()
    assert (target / ".gemini" / "rules" / "frontend_fsd_invariants.md").is_file()

    # Unified Process & Diataxis scaffolds
    assert (target / "architecture" / "README.md").is_file()
    assert (target / "architecture" / "adr" / "0001_initial_fsd_architecture.md").is_file()
    assert (target / "docs" / "README.md").is_file()
    assert (target / "docs" / "tutorials" / "getting_started.md").is_file()

    # Workflows
    assert (target / ".github" / "workflows" / "ci.yml").is_file()
    assert (target / ".github" / "workflows" / "release.yml").is_file()

    # Validate package.json contents
    pkg_content = (target / "package.json").read_text()
    assert "test-app-portal" in pkg_content
    assert "pinia" in pkg_content
    assert "eslint-plugin-boundaries" in pkg_content

    # Execute full build and verification inside docker container
    cmd = "pnpm install && pnpm run type-check && pnpm run lint && pnpm run test && pnpm run build"
    run_node_command_in_docker(target, cmd)


def test_generate_minimal_vue_spa_without_pinia(tmp_path: Path):
    target = tmp_path / "minimal-vue-spa"
    template_root = Path(__file__).parent.parent

    copier.run_copy(
        src_path=str(template_root),
        dst_path=str(target),
        data={
            "app_name": "minimal-ui",
            "app_description": "Minimal UI without Pinia or docs",
            "default_dev_port": 3000,
            "api_base_url_default": "/api/v1",
            "include_pinia_store": False,
            "include_architecture_scaffold": False,
            "include_diataxis_docs": False,
        },
        defaults=True,
        unsafe=True,
    )

    assert (target / "package.json").is_file()
    assert not (target / "src" / "entities" / "user" / "store.ts").exists()
    assert not (target / "architecture").exists()
    assert not (target / "docs").exists()

    pkg_content = (target / "package.json").read_text()
    assert "minimal-ui" in pkg_content
    assert '"pinia"' not in pkg_content

    # Verify building and tests work cleanly without pinia
    cmd = "pnpm install && pnpm run type-check && pnpm run test && pnpm run build"
    run_node_command_in_docker(target, cmd)
