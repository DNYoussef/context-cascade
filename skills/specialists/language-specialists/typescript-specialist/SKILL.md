/*============================================================================*/
/* TYPESCRIPT-SPECIALIST SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: typescript-specialist
version: 1.0.0
description: |
  [assert|neutral] Modern TypeScript development specialist for Node.js backends, Express/Nest.js frameworks, type-safe frontend development, npm package creation, and monorepo management with Turborepo/nx. Use when bui [ground:given] [conf:0.95] [state:confirmed]
category: Language Specialists
tags:
- general
author: system
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute typescript-specialist workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic Language Specialists processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "typescript-specialist",
  category: "Language Specialists",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Aspectual",
  source: "Russian",
  force: "Complete or ongoing?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["typescript-specialist", "Language Specialists", "workflow"],
  context: "user needs typescript-specialist capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# TypeScript Specialist

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Expert TypeScript development for type-safe, scalable backend and full-stack applications with modern tooling.

## Purpose

This skill provides comprehensive TypeScript expertise including advanced type systems, modern Node.js patterns, framework integration (Express, Nest.js), and production-grade TypeScript configuration. It ensures TypeScript code leverages the full power of static typing while maintaining developer productivity.

## When to Use This Skill

Activate this skill when:
- Building backend APIs with Express or Nest.js
- Creating type-safe frontend applications
- Developing npm packages or libraries
- Setting up monorepos with Turborepo or nx
- Migrating JavaScript projects to TypeScript
- Configuring strict TypeScript compiler options
- Implementing advanced TypeScript patterns (generics, mapped types, conditional types)
- Optimizing TypeScript build performance

## Prerequisites

**Required Knowledge**:
- JavaScript ES6+ syntax and concepts
- Node.js runtime and npm/yarn/pnpm
- Basic understanding of static typing

**Required Tools**:
- Node.js 18+ installed
- npm, yarn, or pnpm package manager
- Code editor with TypeScript support (VS Code recommended)

**Agent Assignments**:
- `backend-dev`: Primary TypeScript API implementation
- `coder`: General TypeScript development
- `base-template-generator`: Project scaffolding
- `tester`: Jest/Vitest test suite creation
- `code-analyzer`: Type safety and quality analysis

## Core Workflows

### Workflow 1: Nest.js Backend API Development

**Step 1: Initialize Nest.js Project**

Create a production-ready Nest.js project with TypeScript:

```bash
# Install Nest CLI globally
npm install -g @nestjs/cli

# Create new project
nest new my-api --package-manager pnpm

# Navigate to project
cd my-api

# Install additional dependencies
pnpm add @nestjs/config @nestjs/typeorm typeorm pg class-validator class-transformer
pnpm add -D @types/node
```

**Step 2: Configure TypeScript Strict Mode**

```json
// tsconfig.json
{
  "compilerOptions": {
    "module": "commonjs",
    "declaration": true,
    "removeComments": true,
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "allowSyntheticDefaultImports": true,
    "target": "ES2021",
    "sourceMap": true,
    "outDir": "./dist",
    "baseUrl": "./",
    "incremental": true,
    "skipLibCheck": true,
    "strict": true,
    "strictNullChecks": true,
    "noImplicitAny": true,
    "strictBindCallApply": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "esModuleInterop": true,
    "resolveJsonModule": true
  }
}
```

**Step 3: Create Type-Safe DTOs with Class Validator**

```typescript
// src/users/dto/create-user.dto.ts
import { IsEmail, IsString, MinLength, MaxLength } from 'class-validator';
import { ApiProperty } from '@nestjs/swagger';

export class CreateUserDto {
  @ApiProperty({ description: 'User email address' })
  @IsEmail()
  email: string;

  @ApiProperty({ description: 'Username', minLength: 3, maxLength: 50 })
  @IsString()
  @MinLength(3)
  @MaxLength(50)
  username: string;

  @ApiProperty({ description: 'User password', minLength: 8 })
  @IsString()
  @MinLength(8)
  password: string;
}
```

**Step 4: Implement Service with Dependency Injection**

```typescript
// src/users/users.service.ts
import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { User } from './entities/user.entity';
import { CreateUserDto } from './dto/create-user.dto';

@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private readonly usersRepository: Repository<User>,
  ) {}

  async create(createUserDto: CreateUserDto): Promise<User> {
    const user = this.usersRepository.create(createUserDto);
    return await this.usersReposi

/*----------------------------------------------------------------------------*/
/* S4 SUCCESS CRITERIA                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {
  primary: "Skill execution completes successfully",
  quality: "Output meets quality thresholds",
  verification: "Results validated against requirements"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 MCP INTEGRATION                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MCP_INTEGRATION := {
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"]
} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 MEMORY NAMESPACE                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_NAMESPACE := {
  pattern: "skills/Language Specialists/typescript-specialist/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "typescript-specialist-{session_id}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{project_name}",
  WHY: "skill-execution"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 SKILL COMPLETION VERIFICATION                                            */
/*----------------------------------------------------------------------------*/

[direct|emphatic] COMPLETION_CHECKLIST := {
  agent_spawning: "Spawn agents via Task()",
  registry_validation: "Use registry agents only",
  todowrite_called: "Track progress with TodoWrite",
  work_delegation: "Delegate to specialized agents"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 ABSOLUTE RULES                                                           */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>TYPESCRIPT_SPECIALIST_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
