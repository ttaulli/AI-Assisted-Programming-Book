'use client';

import { useState } from 'react';
import Image from 'next/image';
import WeatherSearch from './components/WeatherSearch';
import WeatherDisplay from './components/WeatherDisplay';
import { getWeatherByCity, WeatherData } from './services/weatherApi';

export default function Home() {
  const [weatherData, setWeatherData] = useState<WeatherData | null>(null);
  const [error, setError] = useState<string | undefined>();
  const [isLoading, setIsLoading] = useState(false);

  const handleSearch = async (city: string) => {
    setIsLoading(true);
    setError(undefined);
    
    try {
      const data = await getWeatherByCity(city);
      
      if (!data) {
        setError('Unable to fetch weather data. Please check your API key configuration.');
      } else {
        setWeatherData(data);
      }
    } catch (err) {
      setError('City not found. Please try a different location.');
      setWeatherData(null);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col min-h-screen p-6">
      <header className="mb-8 text-center">
        <h1 className="text-3xl font-bold mb-2 text-gray-800 dark:text-white">Weather Forecast</h1>
        <p className="text-gray-600 dark:text-gray-300">
          Get real-time weather information for any city
        </p>
      </header>

      <main className="flex-1 flex flex-col items-center justify-start w-full max-w-3xl mx-auto">
        <WeatherSearch onSearch={handleSearch} isLoading={isLoading} />
        
        {isLoading && !weatherData && (
          <div className="mt-10 flex justify-center">
            <div className="loader h-12 w-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
          </div>
        )}
        
        <WeatherDisplay weatherData={weatherData} error={error} />
        
        {!weatherData && !isLoading && !error && (
          <div className="mt-10 text-center text-gray-500 dark:text-gray-400">
            <div className="mb-4">
              <Image 
                src="/globe.svg" 
                alt="Weather Globe" 
                width={80} 
                height={80} 
                className="mx-auto opacity-70 dark:invert"
              />
            </div>
            <p>Enter a city name to get the current weather</p>
            <p className="text-sm mt-2">Powered by OpenWeatherMap API</p>
          </div>
        )}
      </main>

      <footer className="mt-auto pt-6 text-center text-sm text-gray-500 dark:text-gray-400">
        <p>
          Data provided by{' '}
          <a 
            href="https://openweathermap.org/api" 
            target="_blank" 
            rel="noopener noreferrer"
            className="underline text-blue-500 hover:text-blue-700 dark:text-blue-400"
          >
            OpenWeatherMap
          </a>
        </p>
      </footer>
    </div>
  );
}
