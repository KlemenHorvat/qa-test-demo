from locust import HttpUser, task, between

class FHIRPatientSearchUser(HttpUser):
    """
    Simulates a clinician searching for patients on a FHIR server.
    """
    wait_time = between(1, 3)  # wait 1-3 seconds between tasks

    @task
    def search_all_patients(self):
        # GET /baseR4/Patient without parameters returns a Bundle
        self.client.get("/baseR4/Patient", name="Search all patients")

    @task(3)  # weight: run this 3x more often than the other tasks
    def search_patient_by_name(self):
        # Simulate searching by name (common FHIR query)
        self.client.get("/baseR4/Patient?name=Smith", name="Search by name")
        