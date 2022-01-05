import React from 'react';
import {Form} from "semantic-ui-react";
import {Button} from "semantic-ui-react";
import PropTypes from 'prop-types';
import styles from './Login.scss';

// const Login = props => (
// 	<div>This is a component called Login.</div>
// );

// todo: Unless you need to use lifecycle methods or local state,
// write your component in functional form as above and delete
// this section. 
const axios = require('axios');

class Login extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
      username: "",
      password: "",
    };
	}
  attemptLogin(username, password) {
    return [true, "Login Successful"];
  }
  handleFailedLogin(errMsg) {
    alert(errMsg)
  }
  handleSubmit(event, handleSuccessfulLogin) {
    event.preventDefault();
    var loginErr = this.attemptLogin(this.state.username, this.state.password)
    if (loginErr[0] === true){
      handleSuccessfulLogin();
    } else {
      this.handleFailedLogin(loginErr[1]);
    }
  }
  validateForm() {
    return this.state.username.length > 0 && this.state.password.length > 0;
  }
  handleChange(e){
    this.setState({[e.target.name]:e.target.value});
  }
  render() {
    var handleSuccessfulLogin = this.props.handleSuccessfulLogin;
    return (
      <Form onSubmit={(evt) => this.handleSubmit(evt, handleSuccessfulLogin)}>
        <Form.Field>
          <input type="text" placeholder='Username' name="username" onChange={(e)=>this.handleChange(e)}/>
        </Form.Field>
        <Form.Field>
          <input type="password" placeholder='Password' name="password" onChange={(e)=>this.handleChange(e)}/>
        </Form.Field>
        <Button type='submit' disabled={!this.validateForm()}>Submit</Button>
      </Form>
    )
  }
}

const LoginPropTypes = {
	// always use prop types!
};

Login.propTypes = LoginPropTypes;

export default Login;
