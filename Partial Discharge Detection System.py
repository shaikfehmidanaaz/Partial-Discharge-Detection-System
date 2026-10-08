class PartialDischargeDetectionSystem:
    def __init__(self, discharge_level, discharge_count, temperature):
        self.discharge_level = discharge_level
        self.discharge_count = discharge_count
        self.temperature = temperature

    def calculate_risk_score(self):
        score = 0

        # Discharge level
        if self.discharge_level > 80:
            score += 40
        elif self.discharge_level > 50:
            score += 25
        elif self.discharge_level > 20:
            score += 10

        # Number of discharge events
        if self.discharge_count > 100:
            score += 30
        elif self.discharge_count > 50:
            score += 20
        elif self.discharge_count > 20:
            score += 10

        # Temperature
        if self.temperature > 90:
            score += 30
        elif self.temperature > 75:
            score += 20
        elif self.temperature > 60:
            score += 10

        return score

    def detect_condition(self):
        score = self.calculate_risk_score()

        if score >= 70:
            return "CRITICAL"
        elif score >= 40:
            return "WARNING"
        elif score >= 15:
            return "LOW PD ACTIVITY"
        else:
            return "NORMAL"

    def display_result(self):
        risk_score = self.calculate_risk_score()
        condition = self.detect_condition()

        print("----- Partial Discharge Detection System -----")
        print(f"Discharge Level   : {self.discharge_level:.2f} pC")
        print(f"Discharge Count   : {self.discharge_count}")
        print(f"Temperature       : {self.temperature:.2f} °C")
        print(f"Risk Score        : {risk_score} / 100")
        print(f"Condition         : {condition}")

        if condition == "CRITICAL":
            print("Alert: High partial discharge activity detected!")
        elif condition == "WARNING":
            print("Warning: Transformer insulation should be inspected.")
        elif condition == "LOW PD ACTIVITY":
            print("Low partial discharge activity detected.")
        else:
            print("Transformer insulation condition is normal.")


# Example input values
discharge_level = 35       # pC
discharge_count = 30       # events
temperature = 65           # °C

detector = PartialDischargeDetectionSystem(
    discharge_level,
    discharge_count,
    temperature
)

detector.display_result()
