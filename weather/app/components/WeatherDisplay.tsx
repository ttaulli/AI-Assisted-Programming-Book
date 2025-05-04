'use client';

import { WeatherData } from '../services/weatherApi';
import Image from 'next/image';

interface WeatherDisplayProps {
  weatherData: WeatherData | null;
  error?: string;
}

export default function WeatherDisplay({ weatherData, error }: WeatherDisplayProps) {
  if (error) {
    return (
      <div className="w-full max-w-md mt-6 p-6 bg-red-50 dark:bg-red-900/20 rounded-lg text-center">
        <p className="text-red-500 dark:text-red-400">{error}</p>
      </div>
    );
  }

  if (!weatherData) return null;

  const iconUrl = `https://openweathermap.org/img/wn/${weatherData.weather[0].icon}@2x.png`;
  const formattedDate = new Date(weatherData.dt * 1000).toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });

  return (
    <div className="w-full max-w-md mt-6 p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-gray-800 dark:text-white">
            {weatherData.name}, {weatherData.sys.country}
          </h2>
          <p className="text-sm text-gray-500 dark:text-gray-400">{formattedDate}</p>
        </div>
        <div className="flex flex-col items-center">
          <img 
            src={iconUrl} 
            alt={weatherData.weather[0].description} 
            width={70} 
            height={70}
            className="w-16 h-16"
          />
          <p className="text-sm capitalize text-gray-600 dark:text-gray-300">
            {weatherData.weather[0].description}
          </p>
        </div>
      </div>

      <div className="mt-4">
        <div className="flex justify-between items-center">
          <div>
            <p className="text-4xl font-bold text-gray-800 dark:text-white">
              {Math.round(weatherData.main.temp)}°C
            </p>
            <p className="text-sm text-gray-600 dark:text-gray-300">
              Feels like: {Math.round(weatherData.main.feels_like)}°C
            </p>
          </div>
          <div className="grid grid-cols-2 gap-4">
            <div className="text-center">
              <p className="text-sm text-gray-500 dark:text-gray-400">Humidity</p>
              <p className="font-semibold text-gray-800 dark:text-white">{weatherData.main.humidity}%</p>
            </div>
            <div className="text-center">
              <p className="text-sm text-gray-500 dark:text-gray-400">Wind</p>
              <p className="font-semibold text-gray-800 dark:text-white">{weatherData.wind.speed} m/s</p>
            </div>
            <div className="text-center">
              <p className="text-sm text-gray-500 dark:text-gray-400">Pressure</p>
              <p className="font-semibold text-gray-800 dark:text-white">{weatherData.main.pressure} hPa</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}