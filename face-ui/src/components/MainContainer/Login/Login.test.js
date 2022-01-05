import React from 'react';
import { shallow, render, mount } from 'enzyme';
import Login from './Login';

describe('Login', () => {
  let props;
  let shallowLogin;
  let renderedLogin;
  let mountedLogin;

  const shallowTestComponent = () => {
    if (!shallowLogin) {
      shallowLogin = shallow(<Login {...props} />);
    }
    return shallowLogin;
  };

  const renderTestComponent = () => {
    if (!renderedLogin) {
      renderedLogin = render(<Login {...props} />);
    }
    return renderedLogin;
  };

  const mountTestComponent = () => {
    if (!mountedLogin) {
      mountedLogin = mount(<Login {...props} />);
    }
    return mountedLogin;
  };  

  beforeEach(() => {
    props = {};
    shallowLogin = undefined;
    renderedLogin = undefined;
    mountedLogin = undefined;
  });

  // Shallow / unit tests begin here
 
  // Render / mount / integration tests begin here
  
});
