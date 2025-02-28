# Ansible Collection - mrmolybdaen.git

This collection provides installation and configuration tasks for different Gitlab CE and Gitlab Runner setups.

The aim of this collection is to move from Infrastructure as Code (IaC) to a Configuration as Code like model as well.
This means host variables can be used to create YAML based configuration which will get translated via Jinja2 templates
into the actual configuration format.

Security is oriented on CIS benchmarks where available and is mostly optimized for web servers with a limited amount of confidential data.

> **IMPORTANT:**
> If your servers are running in an environment with high confidentiality, such as medical, finance, universities or
> military sectors, you need to apply additional measures and may override some roles.

Some roles focus on basic configuration and hardening which is not configurable.
Where possible we use, aside of apparmor, Systemd unit overrides to secure processes. This adds another layer of security
because Systemd will start processes which already have limited capabilities.


Collection documentation can be found here:

## Dependencies

This role depends on several different Python modules which do not come with the `ansible` or `ansible-core` packages.
- netaddr
- bcrypt
- passlib

## Default values

For most variables defined in roles we use defaults. Those defaults are defined where they are used.
You will find them in templates and task files next to the variable.
Unfortunately this means one can not rely on these variable values when they are not defined by the user if one wants to
use a variable somewhere else.
However, templates are a lot more readable doing this.

## Code quality

This collection will provide custom libraries, plugins and modules written in Python and maybe other languages.
To provide a minimum effort in code quality we run `flake8` and `black` in pre-commit-hooks.
We also do so in a CI/CD workflow.
Flake8 runs with `bugbear`, `bandit` and `black` plugins.

To use the hooks defined in `.pre-commit-config.yaml`, you have to install the `pre-commit` package and install the hook.

```shell
# Install pre-commit
pip install pre-commit
# Install the hook
pre-commit install
```

Talking about pipelines, we run sanity, unit and integration tests in a pre-build phase as well as syntax checks and dry-runs
and actual deployments in a post-build stage.

## Roles and Playbooks
