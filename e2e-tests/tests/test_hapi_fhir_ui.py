import re
from playwright.sync_api import Page, expect

PATIENT_BROWSER_URL = "http://hapi.fhir.org/resource?serverId=home_r4&pretty=true&_summary=&resource=Patient"

def test_patient_browser_loads(page: Page):
    """Smoke test: the HAPI FHIR patient browser page loads and shows patient data."""
    # Navigate to the page and wait for network idle
    page.goto(PATIENT_BROWSER_URL)

    # Verify the heading indicates we're on the Patient resource page
    expect(page.locator("h1, h2, h3")).to_contain_text("Patient", timeout=10000)

    # The page should contain a table with patient entries.
    # We can look for the table element that contains resource IDs (e.g., "Patient/").
    table = page.locator("table.table")
    expect(table).to_be_visible(timeout=10000)

    # At least one row with a patient ID should be present.
    # HAPI FHIR UI displays IDs like "12345" in the first column.
    first_row = table.locator("tbody tr").first
    expect(first_row).to_be_visible(timeout=10000)

    # Optionally verify that the row contains text matching a FHIR ID pattern (numeric)
    row_text = first_row.inner_text()
    assert re.search(r'\d+', row_text), f"Expected a numeric patient ID in the first row, got: {row_text}"
    