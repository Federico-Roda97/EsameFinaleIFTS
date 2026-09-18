function TableRow( {riga} ) {

  return (
    <tr>
      <td><i>{riga.id_ordine}</i></td>
      <td>{riga.anno}</td>
      <td>{riga.stato}</td>
      <td>{riga.nome}</td>
      <td>{riga.cognome}</td>

    </tr>
  )

}

export default TableRow