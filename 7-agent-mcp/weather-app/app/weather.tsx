"use client";
import React, { useState } from "react";

interface WeatherData {
  name: string;
  main: { temp: number };
  weather: { description: string }[];
}

export default function WeatherPage() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState<WeatherData | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const fetchWeather = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setWeather(null);
    if (!city.trim()) {
      setError("Please enter a city name.");
      return;
    }
    setLoading(true);
    try {
      const res = await fetch(`/api/weather?city=${encodeURIComponent(city)}`);
      if (!res.ok) {
        throw new Error("City not found or API error.");
      }
      const data = await res.json();
      setWeather(data);
    } catch (err: any) {
      setError(err.message || "Failed to fetch weather data.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 400, margin: "2rem auto", padding: 20, border: "1px solid #eee", borderRadius: 8 }}>
      <h2>Weather App</h2>
      <form onSubmit={fetchWeather} style={{ marginBottom: 20 }}>
        <input
          type="text"
          value={city}
          onChange={e => setCity(e.target.value)}
          placeholder="Enter city name"
          style={{ padding: 8, width: "70%", marginRight: 8 }}
        />
        <button type="submit" style={{ padding: 8 }}>Get Weather</button>
      </form>
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
      {weather && (
        <div style={{ marginTop: 16 }}>
          <h3>{weather.name}</h3>
          <p>Temperature: {weather.main.temp}°C</p>
          <p>Description: {weather.weather[0].description}</p>
        </div>
      )}
    </div>
  );
}
