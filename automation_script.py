import os
import sys

import requests
import urllib3


def required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def main() -> int:
    controller_url = required_env("AVI_CONTROLLER_URL").rstrip("/")
    username = required_env("AVI_USERNAME")
    password = required_env("AVI_PASSWORD")
    tenant_name = os.getenv("AVI_TENANT_NAME", "test-tenant")
    tenant_description = os.getenv("AVI_TENANT_DESCRIPTION", "Created via automation script")
    verify_tls = os.getenv("AVI_VERIFY_TLS", "true").lower() == "true"

    if not verify_tls:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    session = requests.Session()

    try:
        login_response = session.post(
            f"{controller_url}/login",
            json={"username": username, "password": password},
            verify=verify_tls,
            timeout=20,
        )
        login_response.raise_for_status()

        csrf_token = session.cookies.get("csrftoken")
        if csrf_token:
            session.headers.update({"X-CSRFToken": csrf_token, "Referer": controller_url})

        create_response = session.post(
            f"{controller_url}/api/tenant",
            json={"name": tenant_name, "description": tenant_description},
            verify=verify_tls,
            timeout=20,
        )
        create_response.raise_for_status()
    except requests.RequestException as exc:
        print(f"AVI tenant automation failed: {exc}", file=sys.stderr)
        return 1

    print(f"Tenant created successfully: {tenant_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

