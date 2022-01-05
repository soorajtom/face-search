import React from 'react';
import PropTypes from 'prop-types';
import styles from './Header.scss';

const Header = props => (
	<div>Header goes here.</div>
);

// todo: Unless you need to use lifecycle methods or local state,
// write your component in functional form as above and delete
// this section. 
// class Header extends React.Component {
//   render() {
//     return (
// 		<div className="Header">
// 			<span>Header here</span>
// 		</div>
// 	)
//   }
// }

const HeaderPropTypes = {
	// always use prop types!
};

Header.propTypes = HeaderPropTypes;

export default Header;
