import sys

def forecast_2076(material):
    rates = {
        "Polymer": "⚠️ 2076: 95% fragmented into secondary microplastics. High leaching.",
        "Cellulose": "🌱 2076: 100% bio-assimilated. Integrated into river sediment.",
        "Ferrous Metal": "⛓️ 2076: 80% oxidized. Heavy rust flakes; structural loss.",
        "Historical": "🔍 2076: Awaiting classification for precise decay modeling."
    }
    return rates.get(material, "⏳ 2076: General weathering; physical breakdown ongoing.")

if len(sys.argv) > 1:
    print(forecast_2076(sys.argv[1]))
