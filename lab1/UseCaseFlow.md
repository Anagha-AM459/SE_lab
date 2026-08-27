# Use-Case Flow Specification

## Use Case: Match Lost and Found Item

**Primary Actor:** Finder / Owner

### Preconditions

1. The user has submitted a valid lost or found item report.
2. The report contains the required item details such as category, color, description, date, and location.
3. There are active lost or found reports available for comparison.

### Postconditions

1. The system identifies potential matching items.
2. A match probability is calculated for compatible reports.
3. The relevant potential owner or finder is notified of the possible match.

### Main Success Scenario

1. The Finder / Owner submits a lost or found item report.
2. The system validates the submitted item information.
3. The system retrieves active reports that may be compatible with the submitted item.
4. The system compares the item category and color tags.
5. The system compares the geographical proximity between the reported locations.
6. The system calculates the match probability.
7. The system identifies a potential match.
8. The system sends a notification to the relevant user.
9. The user views the potential match and can proceed with the ownership verification process.

### Alternate Flow — No Suitable Match Found

1. The system compares the submitted item with active reports.
2. No report satisfies the matching criteria.
3. The system informs the user that no potential match was found.
4. The system keeps the report active so that it can be matched against future reports.
