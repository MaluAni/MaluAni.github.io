import "./styles.css";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

const icon = L.icon({
  iconSize: [25, 41],
  iconAnchor: [10, 41],
  popupAnchor: [2, -40],
  iconUrl: "https://unpkg.com/leaflet@1.6/dist/images/marker-icon.png",
  shadowUrl: "https://unpkg.com/leaflet@1.6/dist/images/marker-shadow.png"
});

var map = L.map("map", {
  preferCanvas: true
}).setView([51.505, -0.09], 3);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// fetch("https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json")
//   .then((response) => response.json())
//   .then((responseData) => {
//     console.log(responseData.data);
//     const stations = responseData.data.stations;

//     const layerGroup = L.featureGroup().addTo(map);

//     stations.forEach(({ lat, lon, name, address }) => {
//       layerGroup.addLayer(
//         L.marker([lat, lon], { icon }).bindPopup(
//           `Name: ${name}, Address: ${address}`
//         )
//       );
//     });

//     map.fitBounds(layerGroup.getBounds());
//   });

Promise.all([
  fetch(
    "https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json"
  ),
  fetch("https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json")
]).then(async ([response1, response2]) => {
  const responseData1 = await response1.json();
  const responseData2 = await response2.json();

  const data1 = responseData1.data.stations;
  const data2 = responseData2.data.stations;

  const layerGroup = L.featureGroup().addTo(map);

  data1.forEach(({ lat, lon, name, address, station_id: stationId }) => {
    layerGroup.addLayer(
      L.marker([lat, lon], { icon }).bindPopup(
        `<b>Name</b>: ${name}
          <br/>
          <b>Address</b>: ${address}
          <br/>
         <b>Number of bikes available</b>: ${
           data2.find((d) => Number(d.station_id) === Number(stationId))
             .num_bikes_available
         }
      <br/>
     <b>Number of docs available</b>: ${
       data2.find((d) => Number(d.station_id) === Number(stationId))
         .num_docks_available
     }
          `
      )
    );
  });

  map.fitBounds(layerGroup.getBounds());
});