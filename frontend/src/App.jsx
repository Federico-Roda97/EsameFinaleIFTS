import { useState } from 'react'
import './App.css'
import Table from './components/Table'

function App() {

  const [data, setData] = useState([])
  const [citta, setCitta] = useState("")

  async function handleSubmit(event) {
    event.preventDefault()

    let response = await fetch("/api/ordini/" + citta)
    let json = await response.json()

    setData(json)
  }

  return (
    <>
      <h1>Gamenet</h1>
      <form onSubmit={handleSubmit}>
        <input onChange={(e) => { setCitta(e.target.value) }} placeholder="Città" />
        <button>Cerca</button>
      </form>

      <Table data={data} />
    </>
  )
}

export default App
