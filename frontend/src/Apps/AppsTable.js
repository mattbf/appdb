import React, {useState, useEffect} from 'react';
import AppsApi from './AppsApi.js';

function AppsTable() {
  const [AppsData, setAppsData] = useState([])

  useEffect(() => {
    AppsApi.getApps().then(function (result) {
      setAppsData(result.data)
      console.log(result)
    })
  },[])

  return (
    <div>
    <table  className="table">
         <thead  key="thead">
         <tr>
             <th>#</th>
             <th>App</th>
             <th>Website</th>
             <th>launchYear</th>
             <th>Service Type</th>
             <th>Business Model</th>
             <th>Description</th>
             <th>Monitization</th>
             <th>Tags</th>
             <th>createdOn</th>
         </tr>
         </thead>
         <tbody>
         {AppsData.map( app  =>
             <tr  key={app.id}>
             <td>{app.id}  </td>
             <td>{app.name}</td>
             <td><a href={app.website}> {app.website} </a></td>
             <td>{app.launchYear}</td>
             <td>{app.serviceType}</td>
             <td>{app.businessModel}</td>
             <td>{app.description}</td>
             <td>{app.monitization}</td>
             <td>{app.tags}</td>
             <td>{app.createdOn}</td>
             <td>
             <button > Delete</button>
             <a  href={"/app/" + app.id}> Update</a>
             </td>
         </tr>)}
         </tbody>
         </table>
         <button  className="btn btn-primary">Next</button>
    </div>
  )
}

export default AppsTable

 //onClick={(e)=>  this.handleDelete(e,app.id) }
