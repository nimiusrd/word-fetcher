import { h } from 'preact'
import './Tab.css'

const Tab = ({list}) => {
  const l = list.map(item => (
    <li data-json={item} onClick={handleClick}>{`${item}.json`}</li>
  ))
  return (
    <ul id='tab'>
      {l}
    </ul>
  )
}

function handleClick(e) {
  [...e.target.parentElement.children].forEach((item) => {
    document.getElementById(item.dataset.json).classList.remove('visible')
  })
  const t = document.getElementById(e.target.dataset.json)
  t.classList.toggle('visible')
  document.title = `${e.target.dataset.json}.json`
}

export default Tab