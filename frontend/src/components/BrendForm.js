import React from "react";


class BrendForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {name: '', user: []}
    }


    handleUserChange(event){
        if(!event.target.selectedOptions){
            this.setState({
                'user':[]
            })
            return;
        }

        let  users = []
        for (let i = 0; i < event.target.selectedOptions.length;i++){
            users.push(event.target.selectedOptions.item(i).value)

        }
        this.setState({
            'user': users
        })
    }


    handleChange(event){
        this.setState(
            {
                [event.target.name]:event.target.value

            }

        )
         // console.log(event.target.name ,event.target.value)
         // console.log(this.state.name)
         // console.log(this.state.user)
    }


    handleSubmit(event){
        this.props.createBrend(this.state.name,this.state.user)
        // console.log(this.state.name)
        // console.log(this.state.user)
        event.preventDefault()
    }



    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>

                <div className="form-group">
                    <label for="login">name</label>
                    <input type="text" className="form-control" name="name" value={this.state.name}
                           onChange={(event) => this.handleChange(event)}/>
                </div>

                {/*<div className="form-group">*/}
                {/*    <label for="author">author</label>*/}

                {/*    <input type="number" className="form-control" name="author" value={this.state.author}*/}
                {/*           onChange={(event) => this.handleChange(event)}/>*/}

                {/*</div>*/}

                <select name="user" multiple onChange={(event) => this.handleUserChange(event)}>
                    {this.props.users.map((item) => <option value={item.id}> {item.first_name} </option>)}

                </select>


                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );

    }

}

export default BrendForm