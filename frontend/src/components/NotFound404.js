import React from "react";

const BrendItem = ({brend}) => {
    return (
        <tr>
            <td>
                {brend.id}
            </td>
            <td>
                {brend.name}
            </td>
            <td>
                {brend.users}
            </td>
        </tr>
    )
}

const BrendList = ({brends}) => {

    return (
        <table>
            <th>
                Id    
            </th>
            <th>
                Name
            </th>
            <th>
                User
            </th>
            {brends.map((brend) => <BrendItem brend={brend}/>)}
        </table>
    )
}

export default BrendList;