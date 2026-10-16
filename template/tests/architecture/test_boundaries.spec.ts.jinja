import { describe, it, expect } from 'vitest'
import * as fs from 'node:fs'
import * as path from 'node:path'

/**
 * Architectural compliance test suite enforcing Feature-Sliced Design invariants.
 */
describe('FSD Layer Boundary Enforcement', () => {
  const srcDir = path.resolve(__dirname, '../../src')

  function getAllFiles(dir: string, fileList: string[] = []): string[] {
    if (!fs.existsSync(dir)) return fileList
    const files = fs.readdirSync(dir)
    for (const file of files) {
      const filePath = path.join(dir, file)
      if (fs.statSync(filePath).isDirectory()) {
        getAllFiles(filePath, fileList)
      } else if (file.endsWith('.ts') || file.endsWith('.vue')) {
        fileList.push(filePath)
      }
    }
    return fileList
  }

  it('shared/ components and utilities must not import from higher layers', () => {
    const sharedFiles = getAllFiles(path.join(srcDir, 'shared'))
    const forbiddenPatterns = [
      /@\/entities/,
      /@\/features/,
      /@\/pages/,
      /@\/app/,
      /\.\.\/entities/,
      /\.\.\/features/,
      /\.\.\/pages/,
      /\.\.\/app/
    ]

    for (const file of sharedFiles) {
      const content = fs.readFileSync(file, 'utf-8')
      for (const pattern of forbiddenPatterns) {
        expect(
          pattern.test(content),
          `Boundary Violation: ${path.relative(srcDir, file)} violates FSD-TRUTH-01 by importing from higher layers: ${pattern}`
        ).toBe(false)
      }
    }
  })

  it('features/ must not cross-import from other features', () => {
    const featuresDir = path.join(srcDir, 'features')
    if (!fs.existsSync(featuresDir)) return

    const featureSlices = fs
      .readdirSync(featuresDir)
      .filter((f) => fs.statSync(path.join(featuresDir, f)).isDirectory())

    for (const slice of featureSlices) {
      const sliceFiles = getAllFiles(path.join(featuresDir, slice))
      for (const otherSlice of featureSlices) {
        if (otherSlice === slice) continue
        const forbiddenPattern = new RegExp(`@/features/${otherSlice}|\\.\\./${otherSlice}`)
        for (const file of sliceFiles) {
          const content = fs.readFileSync(file, 'utf-8')
          expect(
            forbiddenPattern.test(content),
            `Boundary Violation: Feature "${slice}" cannot cross-import sibling feature "${otherSlice}" in ${path.relative(srcDir, file)}`
          ).toBe(false)
        }
      }
    }
  })

  it('no raw "any" types in application source code', () => {
    const allFiles = getAllFiles(srcDir)
    // Matches ": any", "as any", "<any>"
    const anyPattern = /:\s*any\b|as\s+any\b|<any>/

    for (const file of allFiles) {
      const content = fs.readFileSync(file, 'utf-8')
      expect(
        anyPattern.test(content),
        `Type Safety Violation: Explicit "any" found in ${path.relative(srcDir, file)}`
      ).toBe(false)
    }
  })
})
