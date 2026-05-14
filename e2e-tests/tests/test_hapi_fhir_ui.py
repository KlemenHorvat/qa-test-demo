import re
from playwright.sync_api import Page, expect

PATIENT_BROWSER_URL = "https://hapi.fhir.org/resource?serverId=home_r4&pretty=true&_summary=&resource=Patient"

def test_search_patients_loads(page: Page):
    """Smoke test: search for all patients and verify results appear."""
    # Navigate to the search page
    page.goto(PATIENT_BROWSER_URL)

    # Verify we are on the Patient search page
    expect(page.locator("h1, h2, h3")).to_contain_text("Patient", timeout=10000)

    # Click the Search button to load patient data
    # The HAPI UI has a button with text "Search" (or "Search" inside a form)
    search_button = page.locator("button:has-text('Search')")
    expect(search_button).to_be_visible(timeout=5000)
    search_button.click()

    # Wait for the results table to appear and contain a row with a patient ID
    # We'll look for any link that matches "Patient/..." in its href
    first_patient_link = page.locator("a[href*='Patient/']").first
    expect(first_patient_link).to_be_visible(timeout=15000)

    # Confirm the link text contains at least one digit (patient ID)
    link_text = first_patient_link.inner_text()
    assert re.search(r'\d+', link_text), f"Expected numeric ID in patient link, got: {link_text}"
    