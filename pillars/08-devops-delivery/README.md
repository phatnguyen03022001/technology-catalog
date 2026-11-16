# 08 — DevOps & Delivery

**Scope:** CI/CD, registries, IaC and deployment tools.

[Taxonomy](../../docs/00-taxonomy.md) · [Evaluation matrix](../../docs/01-evaluation-matrix.md)

## Discover by engineering concern

Use these **existing** entries as starting points, not as a required toolchain or proof of feature support. The full service index and provider evidence remain below.

| Need | Existing entry points |
|---|---|
| Continuous integration and test gates | [GitHub Actions](../../providers/github.md), [GitLab CI](../../providers/gitlab.md), [CircleCI](../../providers/circleci.md) |
| Build pipelines and artifact/container registries | [AWS CodeBuild](../../providers/amazon-web-services.md), [GitHub Container Registry](../../providers/github.md), [Harbor](../../providers/harbor.md) |
| Infrastructure as Code and reproducible provisioning | [OpenTofu](../../providers/opentofu.md), [HCP Terraform](../../providers/hashicorp.md), [Pulumi Cloud](../../providers/pulumi.md) |
| Continuous delivery, deployment and release orchestration | [Argo CD](../../providers/argo-cd.md), [Coolify](../../providers/coolify.md), [Vercel CI](../../providers/vercel.md) |
| Runtime hosting and infrastructure resources | [Compute & Runtime — Pillar 01](../01-compute-runtime/README.md); CI/CD tools are not automatically hosting services |
| Secrets and environment configuration | [Identity & Security — Pillar 07](../07-identity-security/README.md); do not treat CI settings as a complete secrets-governance solution |

**Selection gates, not certified features:** Verify build provenance and artifact integrity, credential least privilege, environment separation, promotion controls, rollout/deployment strategy, rollback or recovery, and operational costs against the chosen workload and current official provider evidence. A service appearing here does not demonstrate that it supports all these controls or is production-ready.

## Service index (facts in providers/)

| Service offering | Provider SSOT |
|---|---|
| Amazon ECR Private | [Amazon Web Services](../../providers/amazon-web-services.md) |
| Amazon ECR Public | [Amazon Web Services](../../providers/amazon-web-services.md) |
| Argo CD | [Argo CD](../../providers/argo-cd.md) |
| AWS CodeBuild | [Amazon Web Services](../../providers/amazon-web-services.md) |
| AWS CodePipeline | [Amazon Web Services](../../providers/amazon-web-services.md) |
| Azure Artifacts | [Microsoft Azure](../../providers/azure.md) |
| Azure Pipelines | [Microsoft Azure](../../providers/azure.md) |
| Bitbucket Pipelines | [Bitbucket](../../providers/bitbucket.md) |
| Bitrise Mobile CI | [Bitrise](../../providers/bitrise.md) |
| Buildkite | [Buildkite](../../providers/buildkite.md) |
| CircleCI | [CircleCI](../../providers/circleci.md) |
| Codemagic Mobile CI | [Codemagic](../../providers/codemagic.md) |
| Coolify | [Coolify](../../providers/coolify.md) |
| Dagger Cloud | [Dagger](../../providers/dagger.md) |
| Depot | [Depot](../../providers/depot.md) |
| Docker Desktop | [Docker](../../providers/docker.md) |
| Docker Hub Personal | [Docker](../../providers/docker.md) |
| Expo EAS Build | [Expo](../../providers/expo.md) |
| GitHub Actions | [GitHub](../../providers/github.md) |
| GitHub Container Registry (GHCR) | [GitHub](../../providers/github.md) |
| GitLab CI (SaaS) | [GitLab](../../providers/gitlab.md) |
| Google Artifact Registry | [Google Cloud & Firebase](../../providers/google.md) |
| Google Cloud Build | [Google Cloud & Firebase](../../providers/google.md) |
| Harbor Container Registry | [Harbor](../../providers/harbor.md) |
| Harness CI | [Harness](../../providers/harness.md) |
| HCP Terraform | [IBM Vault / HashiCorp](../../providers/hashicorp.md) |
| Jenkins | [Jenkins](../../providers/jenkins.md) |
| OpenTofu | [OpenTofu](../../providers/opentofu.md) |
| Pulumi Cloud | [Pulumi](../../providers/pulumi.md) |
| Vercel CI | [Vercel](../../providers/vercel.md) |

## Watchlist — 0 chưa xác minh giá/free tier

| Candidate | Status | Note |
|---|---|---|
