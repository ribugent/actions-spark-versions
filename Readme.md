# Spark Releases (unofficial) Mirroring

Apache Spark releases are distributed through the Apache CDN and archive host. While this system works well for general downloads, it can sometimes be slow or unreliable when running automated tests in CI/CD pipelines, particularly in GitHub Actions.

This repository maintains a mirror of official Apache Spark releases on GitHub Releases, providing a more reliable and faster download source for GitHub Actions workflows. By using this mirror, you can:

- Reduce workflow execution time by downloading from GitHub's infrastructure
- Avoid potential timeouts or failures due to slow mirror responses
- Maintain consistent download speeds across all your workflow runs

The mirroring process is automated and ensures that the files are identical to those available from the official Apache sources.

## Usage

To use the mirrored Spark releases with the action hosted at [vemonet/setup-spark](https://github.com/vemonet/setup-spark), follow these steps:

1. **Create a GitHub Actions workflow**: Add a new workflow file (e.g., `.github/workflows/spark-workflow.yml`) to your repository.

2. **Define the workflow**: Use the following example to define your workflow:

    ```yaml
    name: Spark workflow

    on: [pull_request]

    jobs:
      spark:
        runs-on: ubuntu-latest

        steps:
        - name: Setup Java
          uses: actions/setup-java@v3
          with:
            java-version: '8'
            distribution: zulu

        - name: Setup Spark
          uses: vemonet/setup-spark@v1
          with:
            spark-version: '3.5.1'  # Replace with the desired Spark version
            spark-url: 'https://github.com/ribugent/actions-spark-versions/releases/download/v3.5.1/spark-3.5.1-bin-hadoop3.tgz'  # Replace with your mirror repository URL

        - name: Verify Spark installation
          run: |
            spark-submit --version
    ```

## Disclaimer

This repository is not affiliated with the Apache Software Foundation or the Apache Spark project. It is a mirror of the official Apache Spark releases on GitHub Releases. I am not responsible for the security of the downloaded files - users should verify file integrity and authenticity after downloading if they want to ensure the files are safe and unmodified.

## Security

To ensure the integrity of the mirrored files, anyone can verify that the files are identical to those available on the official Apache Spark CDN. This can be done by comparing the checksums of the files downloaded from this repository with those from the Apache Spark CDN.

Additionally, anyone can check the GPG signature with the procedure described at [https://www.apache.org/info/verification.html](https://www.apache.org/info/verification.html).
