import React from 'react';
import PropTypes from 'prop-types';
import styles from './MainContainer.scss';
import Login from './Login';
import Search from './Search';

// const MainContainer = props => (
// 	<div>This is a component called MainContainer.</div>
// );

// todo: Unless you need to use lifecycle methods or local state,
// write your component in functional form as above and delete
// this section. 
class MainContainer extends React.Component {
	constructor(props) {
		super(props);
		this.state = {auth: false};
	}
	render() {
		if (!this.state.auth){
			return(
				<Login />
			);
		} else {
			return(
				<Search/>
			);
		}
	}
}

const MainContainerPropTypes = {
	// always use prop types!
};

MainContainer.propTypes = MainContainerPropTypes;

export default MainContainer;
