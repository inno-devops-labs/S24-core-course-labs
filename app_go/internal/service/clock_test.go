package service

import (
	"reflect"
	"testing"
	"time"
)

func TestClock_GetCurrentTime(t *testing.T) {
	moscowLocation, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		t.Fatal(err)
	}

	type fields struct {
		nowFunc func() time.Time
	}
	type args struct {
		location *time.Location
	}
	tests := []struct {
		name   string
		fields fields
		args   args
		want   time.Time
	}{
		{
			name: "basic",
			fields: fields{
				nowFunc: func() time.Time {
					return time.Time{}
				},
			},
			args: args{location: moscowLocation},
			want: time.Time{}.In(moscowLocation),
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			c := &Clock{
				nowFunc: tt.fields.nowFunc,
			}
			if got := c.GetCurrentTime(tt.args.location); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("GetCurrentTime() = %v, want %v", got, tt.want)
			}
		})
	}
}
