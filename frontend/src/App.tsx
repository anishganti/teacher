import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import '@mantine/core/styles.css';

import { MantineProvider } from '@mantine/core';
import { FullLayout } from './components/layout/FullLayout';

function App() {
  const [count, setCount] = useState(0)

  return (
    <MantineProvider>
        <FullLayout/>
    </MantineProvider>
  )
}

export default App
