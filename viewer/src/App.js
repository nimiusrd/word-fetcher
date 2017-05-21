import { h } from 'preact'
import Rank from './components/Rank.js'
import List from './components/List.js'
import words from './data/words.json'
import data from './data/data.json'
import count from './data/count.json'
import Tab from './components/Tab.js'
import './App.css'

const jsonList = [
  'words',
  'data',
  'count'
]

const App = (() => {
  return (
    <div>
      <Tab list={jsonList}/>
      <List data={data} id={'data'} />
      <List data={words} id={'words'} />
      <Rank data={count} id={'count'} />
    </div>
  )
});

export default App