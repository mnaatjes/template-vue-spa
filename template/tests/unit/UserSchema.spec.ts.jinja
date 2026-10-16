import { describe, it, expect } from 'vitest'
import { UserSchema } from '@/entities/user/model'

describe('User Domain Schema', () => {
  it('validates compliant user payload', () => {
    const validData = {
      id: 'usr_123',
      name: 'Alice Cooper',
      email: 'alice@example.com',
      role: 'admin'
    }
    const result = UserSchema.safeParse(validData)
    expect(result.success).toBe(true)
  })

  it('rejects invalid email address', () => {
    const invalidData = {
      id: 'usr_123',
      name: 'Alice Cooper',
      email: 'not-an-email',
      role: 'admin'
    }
    const result = UserSchema.safeParse(invalidData)
    expect(result.success).toBe(false)
  })

  it('rejects unrecognized user roles', () => {
    const invalidData = {
      id: 'usr_123',
      name: 'Alice Cooper',
      email: 'alice@example.com',
      role: 'super-admin'
    }
    const result = UserSchema.safeParse(invalidData)
    expect(result.success).toBe(false)
  })
})
