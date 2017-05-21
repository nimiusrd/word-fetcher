import { h } from 'preact'
import './List.css'

const List = (({data, id}) => {
  const list = data.map(item => (
    <li>
      {item}
    </li>
  ))
  return (
    <ul id={id} class={"list"}>
      {list}
    </ul>
  )
})

export default List