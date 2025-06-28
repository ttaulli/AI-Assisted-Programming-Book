import { NextRequest, NextResponse } from "next/server";

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const city = searchParams.get("city");
  if (!city) {
    return NextResponse.json({ error: "City is required." }, { status: 400 });
  }
  const apiKey = process.env.OPENWEATHERMAP_API_KEY;
  if (!apiKey) {
    return NextResponse.json({ error: "API key not configured." }, { status: 500 });
  }
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&appid=${apiKey}&units=metric`;
  try {
    const res = await fetch(url);
    if (!res.ok) {
      return NextResponse.json({ error: "City not found or API error." }, { status: 404 });
    }
    const data = await res.json();
    return NextResponse.json({
      name: data.name,
      main: data.main,
      weather: data.weather,
    });
  } catch (err) {
    return NextResponse.json({ error: "Failed to fetch weather data." }, { status: 500 });
  }
}
