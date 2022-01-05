import React from 'react';
import { shallow, render, mount } from 'enzyme';
import MainContainer from './MainContainer';

describe('MainContainer', () => {
  let props;
  let shallowMainContainer;
  let renderedMainContainer;
  let mountedMainContainer;

  const shallowTestComponent = () => {
    if (!shallowMainContainer) {
      shallowMainContainer = shallow(<MainContainer {...props} />);
    }
    return shallowMainContainer;
  };

  const renderTestComponent = () => {
    if (!renderedMainContainer) {
      renderedMainContainer = render(<MainContainer {...props} />);
    }
    return renderedMainContainer;
  };

  const mountTestComponent = () => {
    if (!mountedMainContainer) {
      mountedMainContainer = mount(<MainContainer {...props} />);
    }
    return mountedMainContainer;
  };  

  beforeEach(() => {
    props = {};
    shallowMainContainer = undefined;
    renderedMainContainer = undefined;
    mountedMainContainer = undefined;
  });

  // Shallow / unit tests begin here
 
  // Render / mount / integration tests begin here
  
});
