// Got this from bootstrap

import Table from 'react-bootstrap/Table';

function DataTable(data: any[]) {
    let temp_rows = []
    for (let i = 0; i < data.length; i++) {
        temp_rows.push(<tr key={i}>
            <td> {data[i].id}</ td>
            <td> {data[i].card_key} </td>
            <td> {data[i].card_desc} </td>
            <td> {data[i].current_stage} </td>
            <td> {data[i].wrong_choices} </td>
            <td> {data[i].hidden ? 'true' : 'false'} </td>
            <td> {data[i].created_at} </td>
            <td> {data[i].up_in} </td>
        </tr>)

    }


    return (


        <Table striped bordered hover variant="dark">
            <thead>
                <tr>
                    <th>Card Id</th>
                    <th>Card Value</th>
                    <th>Card Description</th>
                    <th>Current Bucket </th>
                    <th>Wrong answers </th>
                    <th>Card Completed</th>
                    <th>Created At </th>
                    <th>Due in </th>

                </tr>
            </thead>
            <tbody>
                {temp_rows}

            </tbody>
        </Table>

    );
}

export default DataTable;
