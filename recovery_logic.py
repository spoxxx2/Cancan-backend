def determine_path(label, condition):
    edible_keywords = ['Intact', 'Sealed', 'Packaged']
    if label == "Food" and any(k in condition for k in edible_keywords):
        return {
            "category": "Edible Food Recovery",
            "compliance_code": "SB-1383-EFR",
            "action": "Dispatch to Food Bank"
        }
    else:
        return {
            "category": "Organic Waste",
            "compliance_code": "SB-1383-OW",
            "action": "Compost/Upcycle"
        }
