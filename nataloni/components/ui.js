import { useEffect, useState } from "react";
import { Card, CardContent } from "@/components/ui/card";

export default function Flights() {
  const [flights, setFlights] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/flights")
      .then((response) => response.json())
      .then((data) => setFlights(data));
  }, []);

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-4">
      {flights.map((flight) => (
        <Card key={flight.codice} className="p-4">
          <CardContent>
            <h2 className="text-xl font-bold">Volo {flight.codice}</h2>
            <p>Compagnia: {flight.compagnia}</p>
            <p>Durata: {flight.durataMinuti} minuti</p>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
