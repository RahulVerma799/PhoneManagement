import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Contacts from './Component/Contacts'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className=''>
      <Contacts/>
    </div>
  )
}

export default App
