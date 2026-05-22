import { useState } from "react"
import axios from "axios"


function App() {

  const [file, setFile] = useState(null)

  const [result, setResult] = useState(null)


  const handleUpload = async () => {

    if (!file) return

    const formData = new FormData()

    formData.append("file", file)

    const response = await axios.post(

      "http://127.0.0.1:8000/analyze-audio-emergency",

      formData,

      {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      }
    )

    setResult(response.data)
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
          fontSize: "48px"
        }}
      >
        Rakshak AI
      </h1>

      <p
        style={{
          color: "#94a3b8"
        }}
      >
        Real-Time Emergency Intelligence Dashboard
      </p>


      <div
        style={{
          marginTop: "40px"
        }}
      >

        <input
          type="file"
          onChange={(e) =>
            setFile(e.target.files[0])
          }
        />

        <button
          onClick={handleUpload}
          style={{
            marginLeft: "20px",
            backgroundColor: "#ef4444",
            color: "white",
            border: "none",
            padding: "12px 20px",
            borderRadius: "10px",
            cursor: "pointer"
          }}
        >
          Analyze Emergency
        </button>

      </div>


      {
        result && (

          <div
            style={{
              marginTop: "50px",
              display: "grid",
              gridTemplateColumns: "1fr 1fr",
              gap: "20px"
            }}
          >

            <div
              style={{
                backgroundColor: "#1e293b",
                padding: "25px",
                borderRadius: "15px"
              }}
            >
              <h2>Transcription</h2>

              <p
                style={{
                  color: "#facc15"
                }}
              >
                {result.transcribed_text}
              </p>
            </div>

            <div
              style={{
                backgroundColor: "#1e293b",
                padding: "25px",
                borderRadius: "15px"
              }}
            >
              <h2>Emergency</h2>

              <p
                style={{
                  color: "#fb7185"
                }}
              >
                {result.final_emergency_prediction}
              </p>
            </div>

            <div
              style={{
                backgroundColor: "#1e293b",
                padding: "25px",
                borderRadius: "15px"
              }}
            >
              <h2>Severity</h2>

              <p
                style={{
                  color: "#ef4444"
                }}
              >
                {result.detected_severity}
              </p>
            </div>

            <div
              style={{
                backgroundColor: "#1e293b",
                padding: "25px",
                borderRadius: "15px"
              }}
            >
              <h2>Location</h2>

              <p
                style={{
                  color: "#4ade80"
                }}
              >
                {result.detected_location}
              </p>
            </div>

          </div>
        )
      }

    </div>
  )
}

export default App