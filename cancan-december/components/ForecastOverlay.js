import React from 'react';

const ForecastOverlay = ({ objectData }) => {
  const isHighRisk = objectData.weathering_forecast_2076?.danger_level.includes("Critical");
  
  return (
    <div className="absolute inset-0 z-10 flex flex-col justify-end p-6 bg-black/60 backdrop-blur-[8px] transition-all duration-700 hover:backdrop-blur-none group border-2 border-transparent hover:border-green-500/50">
      <div className={`border-l-4 ${isHighRisk ? 'border-red-500' : 'border-green-500'} pl-4 bg-black/40 p-4 rounded-r-lg`}>
        <div className="flex justify-between items-start mb-2">
          <h3 className="text-white font-bold text-xl uppercase tracking-widest">
            {objectData.sub_type} <span className="text-[10px] opacity-50 block">SPECTRAL_ID: {objectData.spectral_fingerprint?.fe_absorption || "POLY-01"}</span>
          </h3>
          <div className="h-4 w-12 bg-green-500/20 rounded flex items-end gap-0.5 p-0.5">
            <div className="w-full bg-green-500 h-1/2 animate-pulse"></div>
            <div className="w-full bg-green-500 h-full animate-pulse delay-75"></div>
            <div className="w-full bg-green-500 h-3/4 animate-pulse delay-150"></div>
          </div>
        </div>
        
        <div className="space-y-1 mb-4">
          <p className="text-white text-xs font-semibold uppercase tracking-tighter">
            2076 Forecast: {objectData.weathering_forecast_2076?.appearance}
          </p>
          <p className={`${isHighRisk ? 'text-red-400' : 'text-green-400'} text-[10px] font-mono`}>
            INTEGRITY: {objectData.weathering_forecast_2076?.structural_integrity} | RISK: {objectData.weathering_forecast_2076?.danger_level}
          </p>
        </div>

        <div className="pt-2 border-t border-white/10 flex justify-between items-center">
          <span className="text-[8px] text-gray-500 font-mono">
            CANCAN (EIN: 39-2261270) | ADAPTIVE MASTER STRATEGY
          </span>
          <span className="text-[8px] bg-white/10 px-1 py-0.5 text-white">BOOST_1.5x</span>
        </div>
      </div>
    </div>
  );
};

export default ForecastOverlay;
