// Code generated by Wire protocol buffer compiler, do not edit.
// Source file: business/correct.proto at 28:1
package me.littlekey.duoyu.model.proto;

import com.squareup.wire.FieldEncoding;
import com.squareup.wire.Message;
import com.squareup.wire.ProtoAdapter;
import com.squareup.wire.ProtoReader;
import com.squareup.wire.ProtoWriter;
import com.squareup.wire.WireField;
import com.squareup.wire.internal.Internal;
import java.io.IOException;
import java.lang.Boolean;
import java.lang.Object;
import java.lang.Override;
import java.lang.String;
import java.lang.StringBuilder;
import okio.ByteString;

public final class PutCorrectResponse extends Message<PutCorrectResponse, PutCorrectResponse.Builder> {
  public static final ProtoAdapter<PutCorrectResponse> ADAPTER = new ProtoAdapter_PutCorrectResponse();

  private static final long serialVersionUID = 0L;

  public static final Boolean DEFAULT_SUCCESS = false;

  @WireField(
      tag = 1,
      adapter = "com.squareup.wire.ProtoAdapter#BOOL"
  )
  public final Boolean success;

  @WireField(
      tag = 2,
      adapter = "me.littlekey.duoyu.model.proto.Correct#ADAPTER"
  )
  public final Correct correct;

  public PutCorrectResponse(Boolean success, Correct correct) {
    this(success, correct, ByteString.EMPTY);
  }

  public PutCorrectResponse(Boolean success, Correct correct, ByteString unknownFields) {
    super(ADAPTER, unknownFields);
    this.success = success;
    this.correct = correct;
  }

  @Override
  public Builder newBuilder() {
    Builder builder = new Builder();
    builder.success = success;
    builder.correct = correct;
    builder.addUnknownFields(unknownFields());
    return builder;
  }

  @Override
  public boolean equals(Object other) {
    if (other == this) return true;
    if (!(other instanceof PutCorrectResponse)) return false;
    PutCorrectResponse o = (PutCorrectResponse) other;
    return unknownFields().equals(o.unknownFields())
        && Internal.equals(success, o.success)
        && Internal.equals(correct, o.correct);
  }

  @Override
  public int hashCode() {
    int result = super.hashCode;
    if (result == 0) {
      result = unknownFields().hashCode();
      result = result * 37 + (success != null ? success.hashCode() : 0);
      result = result * 37 + (correct != null ? correct.hashCode() : 0);
      super.hashCode = result;
    }
    return result;
  }

  @Override
  public String toString() {
    StringBuilder builder = new StringBuilder();
    if (success != null) builder.append(", success=").append(success);
    if (correct != null) builder.append(", correct=").append(correct);
    return builder.replace(0, 2, "PutCorrectResponse{").append('}').toString();
  }

  public static final class Builder extends Message.Builder<PutCorrectResponse, Builder> {
    public Boolean success;

    public Correct correct;

    public Builder() {
    }

    public Builder success(Boolean success) {
      this.success = success;
      return this;
    }

    public Builder correct(Correct correct) {
      this.correct = correct;
      return this;
    }

    @Override
    public PutCorrectResponse build() {
      return new PutCorrectResponse(success, correct, super.buildUnknownFields());
    }
  }

  private static final class ProtoAdapter_PutCorrectResponse extends ProtoAdapter<PutCorrectResponse> {
    ProtoAdapter_PutCorrectResponse() {
      super(FieldEncoding.LENGTH_DELIMITED, PutCorrectResponse.class);
    }

    @Override
    public int encodedSize(PutCorrectResponse value) {
      return (value.success != null ? ProtoAdapter.BOOL.encodedSizeWithTag(1, value.success) : 0)
          + (value.correct != null ? Correct.ADAPTER.encodedSizeWithTag(2, value.correct) : 0)
          + value.unknownFields().size();
    }

    @Override
    public void encode(ProtoWriter writer, PutCorrectResponse value) throws IOException {
      if (value.success != null) ProtoAdapter.BOOL.encodeWithTag(writer, 1, value.success);
      if (value.correct != null) Correct.ADAPTER.encodeWithTag(writer, 2, value.correct);
      writer.writeBytes(value.unknownFields());
    }

    @Override
    public PutCorrectResponse decode(ProtoReader reader) throws IOException {
      Builder builder = new Builder();
      long token = reader.beginMessage();
      for (int tag; (tag = reader.nextTag()) != -1;) {
        switch (tag) {
          case 1: builder.success(ProtoAdapter.BOOL.decode(reader)); break;
          case 2: builder.correct(Correct.ADAPTER.decode(reader)); break;
          default: {
            FieldEncoding fieldEncoding = reader.peekFieldEncoding();
            Object value = fieldEncoding.rawProtoAdapter().decode(reader);
            builder.addUnknownField(tag, fieldEncoding, value);
          }
        }
      }
      reader.endMessage(token);
      return builder.build();
    }

    @Override
    public PutCorrectResponse redact(PutCorrectResponse value) {
      Builder builder = value.newBuilder();
      if (builder.correct != null) builder.correct = Correct.ADAPTER.redact(builder.correct);
      builder.clearUnknownFields();
      return builder.build();
    }
  }
}
