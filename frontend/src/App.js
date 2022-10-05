import React from 'react';
import axios from "axios";
// import logo from './logo.svg';
import './App.css';
import UserList from "./components/User.js";
import BrendList from "./components/Brend.js";
import NotFound404 from "./components/NotFound404.js";
import BrendForm from "./components/BrendForm";
import LoginForm from "./components/Auth.js";
import Cookies from "universal-cookie";
import {Route, BrowserRouter, Link, Switch, Redirect} from "react-router-dom";
import BrendListUsers from "./components/BrendUser.js";
import user from "./components/User.js";



class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'brends': [],
            'token': '',
        };
    }

    createBrend(name,author){

        const headers = this.get_headers()
        const data = {name:name,users:user}
        axios.post('http://127.0.0.1:8000/api/books/',data,{headers}).then(

            response => {

                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({brends:[]})
        })

    }

    deleteBrend(id){
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/brends/${id}`,{headers}).then(

            response =>{
                this.load_data()

            }
        ).catch(error => {
            console.log(error)
            this.setState({brends: []})
        })
    }



    logout(){
        this.set_token('')
    }
    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users/', {headers}).then(response => {
            this.setState({
                'users': response.data
            })
        }).catch(error => {
            console.log(error)
            this.setState({'users': []})
        })

        axios.get('http://127.0.0.1:8000/api/brends/', {headers}).then(response => {
            this.setState({
                'brends': response.data
            })
        }).catch(error => {
            console.log(error)
            this.setState({'brends': []})
        })
    }
    is_aut(){
        return !!this.state.token
    }
    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token},()=>this.load_data())
        console.log(this.state.token)
        // localStorage.setItem('token',token)
        // let token_ = localStorage.getItem('token')
        // document.cookie = `token=${token},username=nikolay,password=password`

    }

    get_token_from_cookies(){
        const cookies = new Cookies()
        const token =  cookies.get('token')
        this.setState({'token': token},()=>this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {
            username: username,
            password: password
        }).then(response => {
            this.set_token(response.data['token'])
        }).catch(error => console.log(error))

    }

    get_headers(){
        console.log('test')
        let headers = {

            'Content-Type':'application/json',
        }
        if(this.is_aut()){
            headers['Authorization'] = `Token ${this.state.token}`
        }


        return headers
    }

    componentDidMount() {
        this.get_token_from_cookies()
        // this.load_data()
    }


    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'> Users </Link>
                            </li>
                            <li>
                                <Link to='/brends'> Brends </Link>
                            </li>
                            <li>{this.is_aut()?<button onClick={()=> this.logout()}>Logout</button>:
                                <Link to='/login'> Login </Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/brends' component={() => <BrendList brends={this.state.brends}
                                                                              deleteBrend={(id)=> this.deleteBrend(id)}/>}/>

                        <Route exact path='/brends/create' component={() => <BrendForm users={this.state.users}
                                                                              createBrend={(name,user)=> this.createBrend(name,user)}/>}/>


                        <Route path='/user/:id'>

                            <BrendListUsers brends={this.state.brends} users={this.state.users}/>

                        </Route>
                        <Route exact path='/login'
                               component={() => <LoginForm
                                   get_token={(username, password) => this.get_token(username, password)}/>}/>

                        <Redirect from='/users1' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
            </div>
        );
    }
}

export default App;