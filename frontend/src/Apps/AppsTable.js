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
      Table
      {AppsData.map( app =>
        <div key={app.id}> Name: {app.name} </div>
      )}
    </div>
  )
}

export default AppsTable
