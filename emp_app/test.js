//var systemId = {{system.id}}
var systemId = 1;


function getData(url, callback) {
    $.get(url, function(data, status){
        callback(status, data);
    });
}
function postData(url, data, callback) {
    data['csrfmiddlewaretoken'] = '{{csrf_token}}';
    $.post(url, data, function(data, status){
        callback(status, data);
    });
}

function updateUI(uiId, value) {
    document.querySelector(uiId).textContent = value;
}

function getValveNumbers(tankNumber) {
    var indices = [0,1,2,3,4]
    var start = ((tankNumber-1)*5)+1
    return indices.map(function(d){return d+start})
}


///////////////////////////////
function createTag(component, tagPath, id, number){
    var url = '/api/ignition/tags'
    var payload = {
        "component":component ,
        "tag_path":tagPath,
        "id":id,
        "number":number
    };
    postData(url, payload, function(status, data){
        if(status=='success') {
            toastr.success("Tags for Tank added successfully");
        } else {
            toastr.error("Error adding tags for Tank")
        }
    });

}

function createTank(number, water, pressure, temp, moles, flowRate, callback) {
    var url = '/api/ignition/systems/'+systemId+'/tanks';
    var payload = {
        "number": number,
        "water": water,
        "pressure": pressure,
        "temperature": temp,
        "number_of_moles": moles,
        "flow_rate": flowRate
    }
    postData(url, payload, function(status, data){
        callback(status, data);

    });
}


function createPat(tankId, tankNumber){
    var url = '/api/ignition/systems/'+systemId+'/tanks/'+tankId+'/pats';
    var payload = {
        "number": tankNumber,
        "speed": 0,
        "tank": tankId
    }
    postData(url, payload, function(status, data){
        callback(status, data);
    });

}

function createValve(tankId, status, valveNumber){
    var url = '/api/ignition/systems/'+systemId+'/tanks/'+tankId+'/valves';
    var payload = {
        "number": valveNumber,
        "status": status,
        "tank": tankId
    }
    postData(url, payload, function(status, data){
        callback(status, data);
    });
}  

function createStorageTank(number, pressure, temp, moles){
    var url = '/api/ignition/systems/'+systemId+'/stanks';
    var payload = {
        "number": number,
        "pressure": pressure,
        "temperature": temp,
        "number_of_moles":moles
    }
    postData(url, payload, function(status, data){
        callback(status, data);
    });
}

function createSvalve(sTankId, sValveNumber, status){
    var url = '/api/ignition/systems/'+systemId+'/stanks/'+ sTankId+'/s-valves';
    var payload = {
        "number": sValveNumber,
        "status": status,
        "tank": sTankId
    }
    postData(url, payload, function(status, data){
        callback(status, data);
    });
}

//call
//createTank(number, water, pressure, temp, moles, flow_rate, function(status, data) {
//})

//////////////////////////////////////////////////////////////////////////////////////
    $("#tankForm").submit(function(e) {
        var payload = {'system': systemId};
        var inputs = document.forms["tankForm"].getElementsByTagName("input");
        var inputsArray = Array.from(inputs);
        inputsArray.forEach(function(inp){
            if(inp.type === 'number') {
                payload[inp.name] = parseFloat(inp.value);
            } else {
                payload[inp.name] = inp.value;
            }
        })
        // createTank
        // createTank(number, water, pressure, temp, moles, flowRate, callback)
        // if status =='success'
            //createTag on ignition
            //UI update
        // else









////////////////////////////////////////////////////////////////////////////////////// 
    $("#tankForm").submit(function(e) {
        var systemId = {{system.id}}
        payload = {'system': systemId};
        var inputs = document.forms["tankForm"].getElementsByTagName("input");
        var inputsArray = Array.from(inputs);
        inputsArray.forEach(function(inp){
            if(inp.type === 'number') {
                payload[inp.name] = parseFloat(inp.value);
            } else {
                payload[inp.name] = inp.value;
            }
        })



        postData('/api/ignition/systems/'+systemId+'/tanks',
            payload,
            function(status, data){
                if(status=='success') {
                    var tanksCount = {{tanks_count}};
                    toastr.success("Tank added successfully");
                    var tankId = data['id']
                    var tankPath = data['tag_path']



                    payload = {
                        "component": "tank",
                        "tag_path":"{{system.tag_path}}",
                        "id":tankId,
                        "number":data['number']
                    };
                    postData('/api/ignition/tags',payload, function(status, data){
                        if(status=='success') {
                            toastr.success("Tags for Tank added successfully");
                        } else {
                            toastr.error("Error adding tags for Tank")
                        }
                    });

                    getData('/api/ignition/systems/'+systemId+'/tanks', function(status, data){
                        if(status=='success') {
                            tanksCount = data.length;
                            updateUI("#tanksCount", data.length);
                        } else {
                            toastr.error("Error updating Tanks count")
                        }
                    });

                    var tankNumber = data.number;
                    postData('/api/ignition/systems/'+systemId+'/tanks/'+tankId+'/pats',
                        {
                            "number": tankNumber,
                            "speed": 0,
                            "tank": tankId
                        },
                        function(status, data){
                            if(status=='success') {
                                toastr.success("Pat added successfully");
                                var patId = data['id']
                        payload = {
                            "component": "pat",
                            "tag_path":"{{system.tag_path}}/Tank"+ tankNumber +"/",
                            "id":patId,
                            "number":1
                        };
                        postData('/api/ignition/tags',payload, function(status, data){
                            if(status=='success') {
                                toastr.success("Tags for Pat added successfully");
                            } else {
                                toastr.error("Error adding tags for Pat")
                            }
                        });

                                updateUI("#patsCount", tanksCount);
                            } else {
                                cons
                                toastr.error("Error adding Pat")
                            }
                        }
                    )
                    //create valves


                } else {

                    toastr.error("Error adding Tank")
                }
            }
        )
        e.preventDefault();
        $('#createTankModal').modal('hide');
    });

    $("#storageTankForm").submit(function(e) {
        var systemId = {{system.id}}
        payload = {'system': systemId};
        var inputs = document.forms["storageTankForm"].getElementsByTagName("input");
        var inputsArray = Array.from(inputs);
        inputsArray.forEach(function(inp){
            if(inp.type === 'number') {
                payload[inp.name] = parseFloat(inp.value);
            } else {
                payload[inp.name] = inp.value;
            }
        })
        console.log(payload);
        postData('/api/ignition/systems/'+systemId+'/stanks',
            payload,
            function(status, data){
                if(status=='success') {
                    toastr.success("Storage Tank added successfully");
                    //tag creation
                    stankId = data['id']

                    payload = {
                        "component": "stank",
                        "tag_path":"{{system.tag_path}}",
                        "id":stankId,
                        "number":data['number']
                    };
                    postData('/api/ignition/tags',payload, function(status, data){
                        if(status=='success') {
                            toastr.success("Tags for Storage Tank added successfully");
                        } else {
                            toastr.error("Error adding tags for Storage  Tank")
                        }
                    });

                    getData('/api/ignition/systems/'+systemId+'/stanks', function(status, data){
                        if(status=='success') {
                            tanksCount = data.length;
                            updateUI("#stanksCount", data.length);
                        } else {
                            toastr.error("Error updating Storage Tanks count")
                        }
                    });
                } else {
                    cons
                    toastr.error("Error adding Storage Tank")
                }
            }
        );
        e.preventDefault();
        $('#createStorageTankModal').modal('hide');
    });

    function createOptions(parent, tankType, arr) {
        parent.innerHTML = '';
        arr.forEach(function(a){
            var option = document.createElement('option');
            option.textContent = tankType + ' ' + a.number;
            option.value = a.id + '-' + a.number;
            parent.appendChild(option)
        })
        return parent;
    }

    function onTankTypeChanged(e) {
        var systemId = {{system.id}}
        getData('/api/ignition/systems/'+systemId+'/'+e+'s', function(status, data){
            if(status==='success') {
                var arr = data.map(function(x){
                    return {
                        'id': x.id,
                        'number': x.number
                    }
                })
                var optionParent = document.querySelector('#tanksSelect');
                if(e === 'tank') {
                    createOptions(optionParent, 'Tank', arr)
                } else if(e === 'stank') {
                    createOptions(optionParent, 'Storage Tank', arr)
                }
            }
        });
    }

    $("#valveForm").submit(function(e) {
        var systemId = {{system.id}}
        var number = $('input[name=number]', '#valveForm').val();
        var status = $('input[name=status]', '#valveForm').is(':checked');
        var tankType = $('input[name=tanktype]:checked', '#valveForm').val();
        var tankIdNumber = $('select#tanksSelect option:selected', '#valveForm').val();
        var tankId = tankIdNumber.split("-")[0];
        var tankNumber =  tankIdNumber.split("-")[1];


        console.log(tankId)

        if(tankType === 'tank') {
            payload = {
                "number": parseInt(number),
                "status": status,
                "tank": parseInt(tankId)
            }
            postData('/api/ignition/systems/'+systemId+'/tanks/'+tankId+'/valves',
                payload,
                function(stat, data){
                    if(stat === 'success') {
                        toastr.success("Valve added successfully");
                    var valveId = data['id']
                    payload = {
                        "component": "valve",
                        "tag_path":"{{system.tag_path}}/Tank"+ tankNumber +"/",
                        "id":valveId,
                        "number":payload['number']
                    };
                    postData('/api/ignition/tags',payload, function(status, data){
                        if(status=='success') {
                            toastr.success("Tags for valve added successfully");
                        } else {
                            toastr.error("Error adding tags for valve")
                        }
                    });

                        var valveId = data.id;
                        getData('/api/ignition/valve/'+valveId+'/create-tag', function(status, data){
                            if(status=='success') {
                                toastr.success("Tags for Valve added successfully");
                            } else {
                                toastr.error("Error adding tags for Valve")
                            }
                        });
                    } else {
                        toastr.error("Error adding Valve")
                    }
                })
        }
        if(tankType === 'stank') {
            payload = {
                "number": parseInt(number),
                "status": status,
                "stank": parseInt(tankId)
            }
            postData('/api/ignition/systems/'+systemId+'/stanks/'+tankId+'/s-valves',
                payload,
                function(stat, data){
                    if(stat === 'success') {
                        toastr.success("SValve added successfully");

                    var SvalveId = data['id']
                    payload = {
                        "component": "svalve",
                        "tag_path":"{{system.tag_path}}/StorageTank"+ tankNumber +"/",
                        "id": SvalveId,
                        "number":payload['number']
                    };
                    console.log(payload)
                    postData('/api/ignition/tags',payload, function(status, data){
                        if(status=='success') {
                            toastr.success("Tags for SValve added successfully");
                        } else {
                            toastr.error("Error adding tags for SValve")
                        }
                    });


                        var svalveId = data.id;
                        getData('/api/ignition/svalve/'+svalveId+'/create-tag', function(status, data){
                            if(status=='success') {
                                toastr.success("Tags for Valve added successfully");
                            } else {
                                toastr.error("Error adding tags for Valve")
                            }
                        })
                    } else {
                        toastr.error("Error adding Valve")
                    }
                })

        }

        e.preventDefault();
        $('#createValveModal').modal('hide');
    });



