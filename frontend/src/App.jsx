import { useState } from "react"

import axios from "axios"

import {
  ReactMediaRecorder
} from "react-media-recorder"

import {
  MapContainer,
  TileLayer,
  Marker,
  Popup
} from "react-leaflet"

import "leaflet/dist/leaflet.css"

import "leaflet-defaulticon-compatibility"

import "leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css"


function App() {

  const [result, setResult] =
    useState(null)

  const [loading, setLoading] =
    useState(false)

  const [coordinates, setCoordinates] =
    useState([19.0544, 72.8406])


  const fetchCoordinates = async (
    locationName
  ) => {

    try {

      const response = await fetch(

        `https://nominatim.openstreetmap.org/search?format=json&q=${locationName}`

      )

      const data =
        await response.json()

      if (data.length > 0) {

        const lat =
          parseFloat(data[0].lat)

        const lon =
          parseFloat(data[0].lon)

        setCoordinates([lat, lon])
      }

    } catch (error) {

      console.log(error)
    }
  }


  const sendAudioToBackend = async (
    audioBlobUrl
  ) => {

    try {

      setLoading(true)

      const audioBlob = await fetch(
        audioBlobUrl
      ).then((r) => r.blob())

      const formData = new FormData()

      formData.append(
        "file",
        audioBlob,
        "recording.wav"
      )

      const response = await axios.post(

        "http://127.0.0.1:8000/analyze-audio-emergency",

        formData,

        {
          headers: {
            "Content-Type":
              "multipart/form-data"
          }
        }
      )

      setResult(response.data)

      await fetchCoordinates(
        response.data.detected_location
      )

      setLoading(false)

    } catch (error) {

      console.log(error)

      setLoading(false)
    }
  }


  return (

    <div
      style={{
        minHeight: "100vh",
        background:
          "linear-gradient(to bottom right, #020617, #0f172a)",
        color: "white",
        padding: "40px",
        fontFamily: "Arial"
      }}
    >

      <h1
        style={{
          color: "#38bdf8",
          fontSize: "72px",
          textAlign: "center"
        }}
      >
        Rakshak AI
      </h1>

      <p
        style={{
          color: "#94a3b8",
          textAlign: "center",
          marginBottom: "50px",
          fontSize: "20px"
        }}
      >
        Real-Time Emergency Intelligence Dashboard
      </p>


      <ReactMediaRecorder

        audio

        render={({

          startRecording,

          stopRecording,

          mediaBlobUrl

        }) => (

          <div
            style={{
              display: "flex",
              justifyContent: "center",
              gap: "30px"
            }}
          >

            <button

              onClick={startRecording}

              style={{

                backgroundColor: "#22c55e",
                color: "white",
                border: "none",
                padding: "18px 35px",
                borderRadius: "14px",
                cursor: "pointer",
                fontSize: "22px",

                boxShadow:
                  "0 0 20px #22c55e"
              }}
            >
              Start Recording
            </button>


            <button

              onClick={async () => {

                stopRecording()

                setTimeout(async () => {

                  if (mediaBlobUrl) {

                    await sendAudioToBackend(
                      mediaBlobUrl
                    )
                  }

                }, 3000)
              }}

              style={{
                backgroundColor: "#ef4444",
                color: "white",
                border: "none",
                padding: "18px 35px",
                borderRadius: "14px",
                cursor: "pointer",
                fontSize: "22px"
              }}
            >
              Stop & Analyze
            </button>

          </div>
        )}
      />


      <h2
        style={{
          color: "#38bdf8",
          marginTop: "30px",
          textAlign: "center"
        }}
      >
        🎙️ AI Emergency Monitoring Active
      </h2>


      {
        loading && (

          <div
            style={{
              marginTop: "40px",
              color: "white",
              fontSize: "28px",
              fontWeight: "bold",
              textAlign: "center"
            }}
          >
            🚨 Analyzing Emergency...
          </div>
        )
      }


      {
        result && (

          <div
            style={{
              marginTop: "50px",
              display: "grid",
              gridTemplateColumns:
                "1fr 1fr",
              gap: "20px"
            }}
          >

            <div
              style={{
                backgroundColor: "#1e293b",
                padding: "30px",
                borderRadius: "20px",
                textAlign: "center"
              }}
            >
              <h2
                style={{
                  fontSize: "26px"
                }}
              >
                Transcription
              </h2>

              <p
                style={{
                  color: "#facc15",
                  fontSize: "20px"
                }}
              >
                {result.transcribed_text}
              </p>
            </div>


            <div
              style={{
                backgroundColor: "#1e293b",
                padding: "30px",
                borderRadius: "20px",
                textAlign: "center"
              }}
            >
              <h2
                style={{
                  fontSize: "26px"
                }}
              >
                Emergency
              </h2>

              <p
                style={{
                  color: "#fb7185",
                  fontSize: "20px"
                }}
              >
                {
                  result.final_emergency_prediction
                }
              </p>
            </div>


            <div

              style={{

                backgroundColor:
                  result.detected_severity ===
                  "critical"
                    ? "#7f1d1d"
                    : "#1e293b",

                boxShadow:
                  result.detected_severity ===
                  "critical"
                    ? "0 0 25px red"
                    : "none",

                padding: "30px",
                borderRadius: "20px",
                textAlign: "center"
              }}
            >
              <h2
                style={{
                  fontSize: "26px"
                }}
              >
                Severity
              </h2>

              <p
                style={{
                  color: "#ef4444",
                  fontSize: "20px"
                }}
              >
                {result.detected_severity}
              </p>
            </div>


            <div
              style={{
                backgroundColor: "#1e293b",
                padding: "30px",
                borderRadius: "20px",
                textAlign: "center"
              }}
            >
              <h2
                style={{
                  fontSize: "26px"
                }}
              >
                Location
              </h2>

              <p
                style={{
                  color: "#4ade80",
                  fontSize: "20px"
                }}
              >
                {result.detected_location}
              </p>
            </div>

          </div>
        )
      }


      <div
        style={{
          marginTop: "50px"
        }}
      >

        <h2
          style={{
            marginBottom: "20px",
            textAlign: "center",
            fontSize: "40px"
          }}
        >
          Emergency Location Map
        </h2>

        <MapContainer

          center={coordinates}

          zoom={13}

          style={{
            height: "400px",
            width: "100%",
            borderRadius: "20px"
          }}
        >

          <TileLayer
            attribution='&copy; OpenStreetMap contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />

          <Marker position={coordinates}>

            <Popup>

              Emergency detected here

            </Popup>

          </Marker>

        </MapContainer>

      </div>

    </div>
  )
}

export default App