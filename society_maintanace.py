class Resident:
    VALID_STATUSES = ("Paid", "Pending")

    def __init__(self, resident_name: str, flat_number: str, maintenance_fees: float, status: str = "Pending"):
        self.resident_name = resident_name
        self.flat_number = flat_number
        self.maintenance_fees = maintenance_fees
        self.status = self._validate_status(status)

    def _validate_status(self, status: str) -> str:
        normalized = status.strip().capitalize()
        if normalized not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status '{status}'. Must be 'Paid' or 'Pending'.")
        return normalized

    def mark_paid(self) -> None:
        self.status = "Paid"

    def mark_pending(self) -> None:
        self.status = "Pending"

    def display_resident(self) -> None:
        print(f"Flat No: {self.flat_number} | Resident: {self.resident_name} | "
              f"Fees: ₹{self.maintenance_fees:.2f} | Status: {self.status}")


class Society:
    def __init__(self, name: str):
        self.name = name
        self.residents: list[Resident] = []

    def add_resident_record(self, resident: Resident) -> None:
        self.residents.append(resident)
        print(f"Added record for {resident.resident_name} (Flat {resident.flat_number}).")

    def display_all_maintenance_details(self) -> None:
        print(f"\n=== {self.name} - Maintenance Records ===")
        if not self.residents:
            print("No resident records found.")
            return

        for idx, resident in enumerate(self.residents, start=1):
            print(f"{idx}. ", end="")
            resident.display_resident()


# Example usage / test run
if __name__ == "__main__":
    society = Society("Emerald Residency")

    r1 = Resident("Rohan Sharma", "A-101", 2500.0, "Paid")
    r2 = Resident("Sneha Kulkarni", "A-102", 2500.0, "Pending")
    r3 = Resident("Vikram Joshi", "B-204", 3000.0, "Paid")

    society.add_resident_record(r1)
    society.add_resident_record(r2)
    society.add_resident_record(r3)

    society.display_all_maintenance_details()