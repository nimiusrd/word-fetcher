import { h } from 'preact'
import './Rank.css'

const Rank = ({data, id}) => {
  const wordList = []
  for (let [word, score] of data) {
    wordList.push(
    <tr>
      <td>{word}</td>
      <td>{score}</td>
    </tr>
    )
  }
  return (
    <table id={id}>
      {wordList}
    </table>
  )
}

export default Rank