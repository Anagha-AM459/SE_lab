# Community Lost & Found Matching Network

## Problem Context

A community lost-and-found network that extracts visual and text item tags, performs geo-proximity matching between lost and found items, and verifies proof of ownership before revealing contact details.

## Actors

- Finder / Owner
- Community Admin

## Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| FR-001 | Functional | The system shall allow an owner to register a lost item by providing details such as category, description, color, date and location. | High | **Pass:** The lost-item report is successfully stored with all mandatory details. **Fail:** The system accepts a report with missing mandatory information. | Accurate lost-item information is required for matching. |
| FR-002 | Functional | The system shall allow a finder to register a found item by providing details such as category, description, color, date and location. | High | **Pass:** The found-item report is successfully stored. **Fail:** The system accepts a report with missing mandatory information. | Found-item information is required to identify potential matches. |
| FR-003 | Functional | The system shall match newly logged found items with active lost-item reports based on category, color tags and geographical proximity. | High | **Pass:** A match probability is calculated and compatible reports are identified. **Fail:** Incompatible item categories are matched. | Matching lost and found items is the core purpose of the system. |
| FR-004 | Functional | The system shall notify potential owners when a found item has a sufficiently strong match with their lost-item report. | High | **Pass:** A notification is dispatched to the potential owner. **Fail:** No notification is generated for a valid match. | Users need to be informed when a potential match is identified. |
| FR-005 | Functional | The system shall verify a claimant's answers to private security questions before revealing the finder's contact details. | High | **Pass:** Contact details are revealed only after successful verification. **Fail:** Contact details are revealed when verification fails. | Ownership verification helps prevent fraudulent claims and protects privacy. |

## Non-Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| NFR-001 | Security | The system shall protect finder contact information and reveal it only after successful ownership verification. | High | **Pass:** Unauthorized users cannot access contact information. **Fail:** Contact information is displayed before successful verification. | Protects user privacy and reduces unauthorized access. |
| NFR-002 | Performance | The system shall calculate potential matches and return results within the defined target response time under normal and peak usage. | Medium | **Pass:** Benchmarking confirms that the target response time is maintained under simulated peak load. **Fail:** Matching response time consistently exceeds the target. | Fast matching is necessary for the system to be practical for community users. |
