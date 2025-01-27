class SalaryCalculator:
    def __init__(self):
        self.salary_data = {
            'OEP': {
                'January': [1804.73, 180.47, 3980, 1658, 1370, 1340],
                'July': [1804.73, 180.47, 4215, 1658, 1370, 1900]
            },
            'OE': {
                'January': [1715.62, 171.56, 3899, 1447, 1370, 1050],
                'July': [1715.62, 171.56, 4075, 1447, 1370, 1600]
            },
            'CE': {
                'January': [2084.79, 208.48, 4070, 3200, 2200, 2100],
                'July': [2084.79, 208.48, 4535, 3200, 2200, 2500]
            }
        }

    def get_salary_components(self, position, period):
        return sum(self.salary_data[position][period])

    def calculate_salary(self, position, period):
        PENSION_RATE = 14
        AMO_RATE = 2.5
        FOS = 20

        salaire_brut = self.get_salary_components(position, period)
        retenue_pension = salaire_brut * (PENSION_RATE / 100)
        retenue_amo = min(salaire_brut * (AMO_RATE / 100), 400)
        mituelle = min(salaire_brut * 0.01, 100) + min(salaire_brut * 0.015, 80)
        frais_professionnels = self.calcul_frais_pro(salaire_brut)
        
        salaire_net_imposable = salaire_brut - retenue_pension - retenue_amo - mituelle - frais_professionnels
        impots = self.calcul_ir_nv(salaire_net_imposable)
        total_retenus = retenue_pension + retenue_amo + mituelle + impots + FOS
        salaire_net = salaire_brut - total_retenus

        return {
            "salaire_brut": round(salaire_brut, 2),
            "retenue_pension": round(retenue_pension, 2),
            "retenue_amo": round(retenue_amo, 2),
            "retenue_mutuelle": round(mituelle, 2),
            "fos": FOS,
            "salaire_net_imposable": round(salaire_net_imposable, 2),
            "impots": round(impots, 2),
            "total_retenus": round(total_retenus, 2),
            "salaire_net": round(salaire_net, 2)
        }

    def calcul_frais_pro(self, salaire_brut_imposable):
        if salaire_brut_imposable <= 6500:
            return min(salaire_brut_imposable * 0.35, 2275)
        return min(salaire_brut_imposable * 0.25, 2916.67)

    def calcul_ir_nv(self, salaire_net_imposable):
        annual_salary = salaire_net_imposable * 12
        tax_brackets = [
            (40000, 0, 0),
            (60000, 0.10, 40000),
            (80000, 0.20, 60000),
            (100000, 0.30, 80000),
            (180000, 0.34, 100000),
            (float('inf'), 0.37, 180000)
        ]

        total_tax = 0
        for ceiling, rate, floor in tax_brackets:
            if annual_salary > floor:
                taxable_amount = min(annual_salary - floor, ceiling - floor)
                total_tax += taxable_amount * rate
            if annual_salary <= ceiling:
                break

        return total_tax / 12
