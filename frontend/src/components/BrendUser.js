// import React from 'react';
// import { useParams, } from "react-router-dom";
//
//
// const BrendItem = ({brend,users}) => {
//     return (
//         <tr>
//             <td>
//                 {brend.id}
//             </td>
//             <td>
//                 {brend.name}
//             </td>
//             <td>
//                 {brend.users.map((userID) =>{
//                     let user = users.find((users) => users.id === userID)
//
//                     if(user) {
//                         return user.first_name
//                     }
//                 })}
//             </td>
//         </tr>
//     )
// }
//
// const BrendListUsers = ({brends,users}) => {
//
//     let {id} = useParams()
//     console.log(id)
//
//     let filtered_item = brends.filter((brend => brend.users.includes(parseInt(id))))
//
//     return (
//         <table>
//             <th>
//                 Id
//             </th>
//             <th>
//                 Name
//             </th>
//             <th>
//                 User
//             </th>
//             {filtered_item.map((brend) => <BrendItem brend={brend}  users={users}/>)}
//         </table>
//     )
// }
//
// export default BrendListUsers;