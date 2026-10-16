/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution')

module.exports = {
  root: true,
  extends: [
    'plugin:vue/vue3-essential',
    'eslint:recommended',
    '@vue/eslint-config-typescript',
    'plugin:boundaries/recommended'
  ],
  plugins: ['boundaries'],
  parserOptions: {
    ecmaVersion: 'latest'
  },
  settings: {
    'boundaries/elements': [
      { type: 'app', pattern: 'src/app/*' },
      { type: 'pages', pattern: 'src/pages/*' },
      { type: 'features', pattern: 'src/features/*' },
      { type: 'entities', pattern: 'src/entities/*' },
      { type: 'shared', pattern: 'src/shared/*' }
    ]
  },
  rules: {
    'boundaries/element-types': [
      'error',
      {
        default: 'disallow',
        rules: [
          {
            from: 'app',
            allow: ['pages', 'features', 'entities', 'shared']
          },
          {
            from: 'pages',
            allow: ['features', 'entities', 'shared']
          },
          {
            from: 'features',
            allow: ['entities', 'shared']
          },
          {
            from: 'entities',
            allow: ['shared']
          },
          {
            from: 'shared',
            allow: ['shared']
          }
        ]
      }
    ],
    'boundaries/entry-point': [
      'error',
      {
        default: 'allow'
      }
    ],
    '@typescript-eslint/no-explicit-any': 'error'
  }
}
