# 🧪 AVI Load Balancer API Automation (Postman + Python)

This project demonstrates how to configure and automate API operations on the **VMware AVI Load Balancer Controller**, including tenant creation and management using **Postman** and optional **Python scripting**.

---

## 📌 Contents

- ✅ Postman Collection for API calls
- 🛠️ Dummy credentials and tenant names (for security)
- 💻 Optional Python automation script
- 📷 Screenshots for proof of execution

---

## 📂 Project Structure

```
avi-api-automation/
├── avi_postman_collection.json   # All API requests (e.g., Create Tenant)
├── automation_script.py          # Python script using requests (optional)
├── environment.json              # Postman environment file (optional)
└── screenshots/                  # Screenshots of successful API execution
```

---

## 🧪 API Endpoints Included

- `POST /api/tenant` – Create new tenant
- `DELETE /api/tenant/{uuid}` – Delete existing tenant
- `GET /api/tenant` – List all tenants
- `PUT /api/tenant/{uuid}` – Update tenant details

---

## 🚀 How to Use

### ▶️ Run via Postman

1. Open Postman.
2. Import `avi_postman_collection.json`.
3. (Optional) Import `environment.json`.
4. Run requests in sequence:
   - Login → Create Tenant → Verify → Delete Tenant

### 🐍 Run Python Script (Optional)

```bash
python automation_script.py
```

---

## 🛡️ Dummy Data Used

> All sensitive information (IP, username, password) has been replaced with placeholders.

---

## 📷 Screenshots

Find evidence of API responses in the `screenshots/` folder.

---

## 🧠 Skills Applied

- REST API integration
- Postman Collections and Automation
- Basic API scripting using Python (`requests`)
- Cloud networking concepts (multi-tenancy with AVI)

---

## 📬 Contact

Feel free to reach out via GitHub issues for any questions.

## Production Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Operations Guide](docs/OPERATIONS.md)
- [Architecture Diagram](docs/diagrams/architecture.mmd)
- [Workflow Diagram](docs/diagrams/workflow.mmd)
- [Security Policy](SECURITY.md)
- [Contributing Guide](CONTRIBUTING.md)
