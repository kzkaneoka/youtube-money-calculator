import React, { Component } from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import YoutubeDateService from './YoutubeDataService.js';

class ChannelForm extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            channelUrl: ''
        };
        this.validate = this.validate.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
    }

    onSubmit(values) {
        YoutubeDateService.calculate(values.channelUrl);
    }

    validate(values) {
        let errors = {};
        if (!values.channelUrl) {
            errors.url = 'Required';
        }
        return errors;
    }

    render() {
        return (
            <div className='ChannelForm'>
                <Formik
                    initialValues={{ channelUrl: ''}}
                    enableReinitialize={true}
                    validate={this.validate}
                    validateOnChange={false}
                    validateOnBlur={false}
                    onSubmit={this.onSubmit}
                >
                    {
                        (props) => (
                            <Form>
                                <ErrorMessage name='channelUrl'/>
                                <fieldset className='form-group'>
                                    <label>Youtube Channel URL</label>
                                    <Field className='form-control' type='text' name='channelUrl' />
                                </fieldset>
                                <button className='btn btn-success' type='submit'>Calculate Money</button>
                            </Form>
                        )
                    }
                </Formik>
            </div>
        )
    };
}

export default ChannelForm;
