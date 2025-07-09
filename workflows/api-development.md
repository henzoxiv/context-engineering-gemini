# Workflow: REST API Development

## Overview
End-to-end workflow for building production-ready REST APIs with comprehensive testing and documentation.

## Tech Stack
- **Runtime**: Node.js + Express/Fastify
- **Database**: PostgreSQL + Prisma
- **Validation**: Zod
- **Testing**: Jest + Supertest
- **Documentation**: OpenAPI + Swagger

## Phase 1: API Design & Planning

### API Specification
```markdown
## FEATURE:
Design REST API with:
- OpenAPI 3.0 specification
- Resource modeling
- Endpoint planning
- Authentication strategy
- Rate limiting design

## EXAMPLES:
- `examples/patterns/api-design.yaml`
- `examples/patterns/resource-modeling.js`

## DOCUMENTATION:
- REST API best practices: https://restfulapi.net/
- OpenAPI specification: https://swagger.io/specification/
```

## Phase 2: Core Implementation

### Server Setup
```markdown
## FEATURE:
Express.js server with:
- Middleware stack (CORS, helmet, compression)
- Error handling
- Request logging
- Health checks
- Graceful shutdown

## EXAMPLES:
- `examples/patterns/server-setup.js`
- `examples/patterns/middleware.js`
- `examples/patterns/error-handling.js`
```

### Database Integration
```markdown
## FEATURE:
Database layer with:
- Prisma schema design
- Migration scripts
- Connection pooling
- Transaction management
- Database seeding

## EXAMPLES:
- `examples/integrations/databases/prisma-advanced/`
- `examples/patterns/transaction-patterns.js`
```

### Authentication & Authorization
```markdown
## FEATURE:
Security implementation with:
- JWT token management
- Role-based access control
- API key authentication
- OAuth 2.0 integration
- Security headers

## EXAMPLES:
- `examples/patterns/auth-strategies.js`
- `examples/patterns/rbac.js`
- `examples/testing/unit/auth.test.js`
```

## Phase 3: Advanced Features

### Caching Strategy
```markdown
## FEATURE:
Multi-layer caching with:
- Redis integration
- Application-level caching
- Database query caching
- CDN integration
- Cache invalidation

## EXAMPLES:
- `examples/integrations/message-queues/redis-caching.js`
- `examples/patterns/cache-strategies.js`
```

### Background Jobs
```markdown
## FEATURE:
Asynchronous processing with:
- Bull Queue (Redis)
- Job scheduling
- Error handling & retries
- Job monitoring
- Dead letter queues

## EXAMPLES:
- `examples/integrations/message-queues/bull-setup.js`
- `examples/patterns/job-patterns.js`
```

### File Upload & Storage
```markdown
## FEATURE:
File management with:
- Multer file upload
- AWS S3 integration
- Image processing
- File validation
- Virus scanning

## EXAMPLES:
- `examples/integrations/external-apis/aws-s3.js`
- `examples/patterns/file-processing.js`
```

## Phase 4: Testing & Quality

### Comprehensive Testing
```markdown
## FEATURE:
Full test suite with:
- Unit tests (business logic)
- Integration tests (API endpoints)
- Contract tests (API schema)
- Load tests (performance)
- Security tests (OWASP)

## EXAMPLES:
- `examples/testing/integration/api-endpoints.test.js`
- `examples/testing/unit/business-logic.test.js`
- `examples/testing/e2e/api-contracts.test.js`
```

### API Documentation
```markdown
## FEATURE:
Interactive documentation with:
- Swagger UI generation
- Code examples
- Authentication flows
- Error response examples
- Postman collection export

## EXAMPLES:
- `examples/patterns/swagger-config.js`
- `examples/patterns/api-docs.js`
```

## Phase 5: Production Readiness

### Performance Optimization
```markdown
## FEATURE:
Performance tuning with:
- Response compression
- Database query optimization
- Connection pooling
- Memory profiling
- Benchmarking

## EXAMPLES:
- `examples/patterns/performance-optimization.js`
- `examples/patterns/database-optimization.js`
```

### Monitoring & Observability
```markdown
## FEATURE:
Production monitoring with:
- Structured logging
- Metrics collection (Prometheus)
- Distributed tracing
- Error tracking
- Performance monitoring

## EXAMPLES:
- `examples/patterns/observability.js`
- `examples/patterns/metrics.js`
```

### Deployment
```markdown
## FEATURE:
Production deployment with:
- Docker containerization
- Kubernetes manifests
- CI/CD pipeline
- Blue-green deployment
- Rollback strategy

## EXAMPLES:
- `examples/integrations/deployment/k8s-api.yaml`
- `examples/integrations/deployment/api.dockerfile`
```

## Success Criteria
- [ ] API handles 1000+ requests/second
- [ ] Response time <100ms for 95th percentile
- [ ] 99.9% uptime
- [ ] Zero security vulnerabilities
- [ ] 100% API documentation coverage
- [ ] Automated deployment pipeline

## Common Pitfalls to Avoid
- Not validating input data
- Missing error handling
- Poor database query patterns
- Inadequate testing coverage
- Missing authentication
- No rate limiting
- Poor logging practices

## Timeline
- **Week 1**: Design, server setup, basic CRUD
- **Week 2**: Authentication, advanced features
- **Week 3**: Testing, documentation, optimization
- **Week 4**: Deployment, monitoring, final testing
