# Workflow: Web Application Starter

## Overview
Complete workflow for building a modern web application from scratch using context engineering principles.

## Prerequisites
- Node.js 18+
- React/Next.js knowledge
- Database choice (PostgreSQL recommended)

## Phase 1: Project Setup & Architecture

### Initial Context Setup
```bash
# In Gemini CLI
/generate-prp workflows/web-app-starter.md
```

### Required Context
- **Tech Stack**: React + Next.js + TypeScript + Tailwind + PostgreSQL
- **Architecture**: Clean architecture with domain-driven design
- **Examples**: Reference `examples/architectures/clean-architecture/`
- **Patterns**: Reference `examples/patterns/api-integration.py`

## Phase 2: Feature Implementation

### Authentication System
```markdown
## FEATURE:
Implement JWT-based authentication with:
- User registration/login
- Password reset flow
- Role-based access control
- Session management

## EXAMPLES:
- `examples/integrations/databases/user-model.js`
- `examples/patterns/auth-middleware.js`
- `examples/testing/unit/auth.test.js`

## DOCUMENTATION:
- NextAuth.js: https://next-auth.js.org/
- JWT best practices: https://auth0.com/blog/a-look-at-the-latest-draft-for-jwt-bcp/
```

### API Layer
```markdown
## FEATURE:
Create RESTful API with:
- CRUD operations for main entities
- Input validation and sanitization
- Error handling middleware
- API documentation with OpenAPI

## EXAMPLES:
- `examples/architectures/clean-architecture/api/`
- `examples/patterns/validation.js`
- `examples/testing/integration/api.test.js`
```

### Database Layer
```markdown
## FEATURE:
Database integration with:
- Prisma ORM setup
- Migration system
- Seed data
- Connection pooling

## EXAMPLES:
- `examples/integrations/databases/prisma-setup/`
- `examples/patterns/repository-pattern.js`
```

## Phase 3: Frontend Implementation

### UI Components
```markdown
## FEATURE:
Reusable component library with:
- Design system implementation
- Accessibility compliance
- Responsive design
- Storybook documentation

## EXAMPLES:
- `examples/patterns/component-patterns.jsx`
- `examples/testing/unit/components.test.jsx`
```

### State Management
```markdown
## FEATURE:
Client-side state management with:
- Global state (Zustand)
- Server state (React Query)
- Form state (React Hook Form)
- Local storage persistence

## EXAMPLES:
- `examples/patterns/state-management.js`
- `examples/patterns/api-client.js`
```

## Phase 4: Testing & Quality

### Test Suite
```markdown
## FEATURE:
Comprehensive testing with:
- Unit tests (Jest + Testing Library)
- Integration tests (Supertest)
- E2E tests (Playwright)
- Performance tests

## EXAMPLES:
- `examples/testing/unit/`
- `examples/testing/integration/`
- `examples/testing/e2e/`
```

### Code Quality
```markdown
## FEATURE:
Code quality setup with:
- ESLint + Prettier
- Husky pre-commit hooks
- TypeScript strict mode
- SonarQube integration

## EXAMPLES:
- `examples/patterns/code-quality-config/`
```

## Phase 5: Deployment & DevOps

### CI/CD Pipeline
```markdown
## FEATURE:
Automated deployment with:
- GitHub Actions workflow
- Docker containerization
- Database migrations
- Environment management

## EXAMPLES:
- `examples/integrations/deployment/github-actions.yml`
- `examples/integrations/deployment/Dockerfile`
```

### Monitoring & Observability
```markdown
## FEATURE:
Production monitoring with:
- Application logging (Winston)
- Error tracking (Sentry)
- Performance monitoring (New Relic)
- Health checks

## EXAMPLES:
- `examples/patterns/logging.js`
- `examples/patterns/monitoring.js`
```

## Success Criteria
- [ ] Application loads in <2 seconds
- [ ] 100% test coverage on critical paths
- [ ] Zero accessibility violations
- [ ] Zero security vulnerabilities
- [ ] Automated deployment pipeline
- [ ] Production monitoring active

## Timeline
- **Week 1**: Project setup, auth, basic API
- **Week 2**: Frontend components, state management
- **Week 3**: Advanced features, testing
- **Week 4**: Deployment, monitoring, optimization

## Next Steps
After completion, use this app as a reference in `examples/architectures/web-app-complete/`
